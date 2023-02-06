import os
import json
import yaml



"""
Function get ending of file
example: from 'gendiff/tree1.json' get '.json'.
"""


def get_ending(pathfile):
    return os.path.splitext(pathfile)[1]


"""
Open file and get parsing_data.
"""


def get_data(pathfile):
    with open(pathfile, 'r') as data:
        return parsing_data(data, get_ending(pathfile))


def parsing_data(data, ending):
    try:
        if ending == '.yaml' or '.yml':
            data_dict = yaml.load(data, Loader=yaml.FullLoader)
        elif ending == '.json':
            data_dict = json.load(data)

        if data_dict is None:
            raise TypeError     # поднять TypeError
    except (TypeError, yaml.parser.ParserError):
        return False
    else:
        return data_dict



# variable for manual checking


"""pathfile2 = '/Users/pavelminaev/python-project-lvl2/tests/fixtures/tree_files/tree1.json'


print(get_data(pathfile2))"""
