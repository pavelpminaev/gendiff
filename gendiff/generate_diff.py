"""Modul search difference between two collections"""

import json


"""
f1 = open('file1.json', 'r')
f2 = open('file2.json', 'r')
"""


with open('file1.json', 'r') as first_collection:
    with open('file2.json', 'r') as second_collection:
        for key, value in first_collection:
            result = []
            if first_collection[key] != second_collection[key]:
                print(result.append(f'{key}{value}'))




"""keys1 = first_collection.keys()
keys2 = second_collection.keys()"""

"""for key, value in first_collection:
    result = []"""

"""
def searcher_diff(key):
    key = first_collection
    if first_collection[key] not in second_collection[key]:
        return print(result.append(f'{key}{value}')
"""



"""def make_format(diff_dict):
    return json.dumps(diff_dict, indent=3, sort_keys=True)"""



