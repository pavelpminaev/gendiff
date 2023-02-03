"""Modul search difference between two collections"""

import gendiff

with open(file1.json, 'r') as first_collection:
    with open(file2.json, 'r') as second_collection:
        for key, value in first_collection:
            result = []
            if first_collection[key] != second_collection[key]:
                print(result.append(f'{- }{key}{value} second_collection)
