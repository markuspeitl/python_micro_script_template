#!/usr/bin/env python3

import os
from pathlib import PurePath
import sys


def print_exec_cmd(cmd: str):
    print(cmd)
    os.system(cmd)


def is_direct_exec():
    script_file_path_obj = PurePath(__file__)
    return script_file_path_obj.name in sys.argv[0]


def get_package_dir_arg_or_relative_default():
    # Check if the script is directly called (file name is in argv) -> otherwise assume installed through console_scripts
    if (is_direct_exec()):
        script_dir: str = os.path.dirname(os.path.realpath(__file__))
        package_dir: str = os.path.dirname(os.path.realpath(script_dir))
        # print(f"Script dir: {script_dir}")
        return package_dir

    if (len(sys.argv) > 1):
        return os.path.realpath(sys.argv[1])

    return None


def main():
    package_dir: str = get_package_dir_arg_or_relative_default()
    print(f"Package dir: {package_dir}")

    build_py_target = f'py_build {package_dir}'
    if (is_direct_exec()):
        build_py_target = "python3 " + os.path.join(os.path.realpath(package_dir), './package/build.py')

    print_exec_cmd(f'{build_py_target}')
    print_exec_cmd(f'twine check {package_dir}/dist/*')
    print_exec_cmd(f'twine upload {package_dir}/dist/*')
    # twine upload -r testpypi dist/*


if __name__ == '__main__':
    sys.exit(main())
