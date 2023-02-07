"""Module for parsing data from .yml and .json files.
"""
import _io
import os
import json
import yaml


def get_ending(pathfile: str) -> str:
    """
    Function get ending of file
    example: from 'gendiff/tree1.json' get '.json'.
    """
    return os.path.splitext(pathfile)[1]


def get_data(pathfile: str) -> str:
    """
    Open file and get parsing_data.
    """
    with open(pathfile, 'r') as data:
        print(type(data))
        return parsing_data(data, get_ending(pathfile))


def parsing_data(data: _io.TextIOWrapper, ending: str) -> dict:
    """
    Checking opening file and return dictionary
    with data of .json or .yml file
    """
    try:
        if ending == '.yaml' or '.yml':
            data_dict = yaml.load(data, Loader=yaml.FullLoader)
        elif ending == '.json':
            data_dict = json.load(data)
        if data_dict is None:
            raise TypeError  # поднять TypeError
    except (TypeError, yaml.parser.ParserError):
        return False
    else:
        return data_dict


# variable for manual checking
pathfile2 = '/Users/pavelminaev/python-project-lvl2/tests/fixtures/tree_files/tree1.json'
print(type(get_data(pathfile2)))
