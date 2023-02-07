"""Module for parsing data_of_file from .yml and .json files."""

import json
import os
import yaml


def get_ending(pathfile: str) -> str:
    """Function get ending of file."""

    return os.path.splitext(pathfile)[1]


def parsing_data(data_of_file, ending: str) -> dict or bool:
    """Checking opening file and return dictionary
    with data_of_file of .json or .yml file.
    """

    data_dict = {}
    try:
        if ending == '.yaml' or '.yml':
            data_dict = yaml.load(data_of_file, Loader=yaml.FullLoader)
        elif ending == '.json':
            data_dict = json.load(data_of_file)
        if data_dict is None:
            raise TypeError  # поднять TypeError
    except (TypeError, yaml.parser.ParserError):
        return False
    else:
        return data_dict


def get_data(pathfile: str) -> dict:
    """Open file and get parsing_data."""

    with open(pathfile, 'r') as data_of_file:
        return parsing_data(data_of_file, get_ending(pathfile))
