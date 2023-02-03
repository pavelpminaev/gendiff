#!/usr/bin/env python3
"""Script....."""

import argparse
from gendiff import generate_diff

def main():
    """..."""
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
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
