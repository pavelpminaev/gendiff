#!/usr/bin/env python
"""Script for compare two configuration files and shows a difference."""

import argparse
from gendiff.generator_of_diff import generate_diff


def main():

    parser = argparse.ArgumentParser(description='Compares two configuration '
                                                 'files and shows '
                                                 'a difference.')

    parser.add_argument('first_file',
                        type=str,
                        help='first file for comparison')
    parser.add_argument('second_file',
                        type=str,
                        help='second file for comparison')
    parser.add_argument('-f', '--format',
                        type=str,
                        default='json',
                        help='set format of output (default: JSON)')

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
