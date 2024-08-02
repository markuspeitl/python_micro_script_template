import argparse
import sys
from typing import Any


def my_program_function(config: dict[str, Any] = {}):
    print('Hello world from python micro script template')


def add_script_parsing_options(parser: argparse.ArgumentParser):
    parser.add_argument('source_path', help="")
    parser.add_argument('-id', '--input_dir', help="")
    parser.add_argument('-m', '-multi', '--multi_args', nargs="+", help="")
    parser.add_argument('-d', '--default', help="", default='default value', choices=['default value', 'other value'])


def main(parser: argparse.ArgumentParser | None = None):
    parser_description = "My script description"

    if (not parser):
        parser = argparse.ArgumentParser(
            description=parser_description
        )
        add_script_parsing_options(parser)

    args: argparse.Namespace = parser.parse_args()

    config: dict[str, Any] = vars(args)
    my_program_function(config)


if __name__ == '__main__':
    sys.exit(main())
