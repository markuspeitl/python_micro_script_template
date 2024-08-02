#!/usr/bin/env python3

import os
import re
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
setup_py = os.path.realpath(os.path.join(script_dir, 'setup.py'))

selected_protocol = 'ssh'
if (len(sys.argv) > 1):
    selected_protocol = sys.argv[1]

print(f"Selected protocol: {selected_protocol}")


def extract_setup_url_value():
    read_file: str | None = None
    with open(setup_py, "r") as file_reader:
        read_file = file_reader.read()

    if (not read_file):
        exit()

    match_url_regex = re.compile('url\s*=\s*"(.+)"')

    matched_url_field = re.search(match_url_regex, read_file)
    # print(matched_url_field)
    # print(matched_url_field.group(0))
    # print(matched_url_field.group(1))

    matched_url = matched_url_field.group(1)
    return matched_url


matched_url = extract_setup_url_value()


if (not matched_url.startswith('http')):
    raise Exception("Error only http prefixed urls are supported")

after_protocol_url = re.sub(r'^(http://|https://)', '', matched_url)

domain_url_parts = after_protocol_url.split('/')
domain = domain_url_parts[0]
after_domain_parts = domain_url_parts[1:]
after_domain_parts_joined = '/'.join(after_domain_parts)

if (selected_protocol in ['http', 'https']):
    http_target = f"git+https://{domain}/{after_domain_parts_joined}.git"
    cmd = f'pip3 install "{http_target}"'
    print(cmd)
    os.system(cmd)
    exit()


ssh_target = f"git+ssh://git@{domain}/{after_domain_parts_joined}.git"

cmd = f'pip3 install "{ssh_target}"'
print(cmd)
os.system(cmd)

# pip3 install git+ssh://git@github.com/markuspeitl/python_micro_script_template.git
# pip3 install git+https://github.com/markuspeitl/python_micro_script_template.git
