#!/usr/bin/env python3

import os

script_dir = os.path.dirname(os.path.realpath(__file__))

os.system(f'pip install -e {script_dir}')
