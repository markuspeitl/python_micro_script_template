#!/usr/bin/env python3

import os
script_dir = os.path.dirname(os.path.realpath(__file__))

os.system(f'python3 {script_dir}/build.py')
os.system(f'twine check {script_dir}/dist/*')
os.system(f'twine upload {script_dir}/dist/*')
# twine upload -r testpypi dist/*
