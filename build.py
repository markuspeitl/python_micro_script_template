#!/usr/bin/env python3

import os
script_dir = os.path.dirname(os.path.realpath(__file__))

os.system(f'rm {script_dir}/dist/*')
os.system(f'python3 {script_dir}/setup.py sdist bdist_wheel')
