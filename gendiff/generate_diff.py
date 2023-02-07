"""Modul search difference between two collections"""

from gendiff.parsing import get_data


def make_diff(node1, node2):

    def get_difference(key):

        if key in deleted_keys:
            val = {'type': 'deleted', 'value': node1[key]}

        elif key in added_keys:
            val = {'type': 'added', 'value': node2[key]}

        elif key in changed_keys and node1[key] == node2[key]:
            val = {'type': 'unchanged', 'value': node1[key]}

        elif key in changed_keys and node1[key] != node2[key]:
            if isinstance(node1[key], dict) and isinstance(node2[key], dict):
                val = {'type': 'internal_change',
                       'value': make_diff(node1[key], node2[key])}
            else:
                val = {'type': 'changed_value',
                       'value': [node1[key], node2[key]]}
        return key, val

    all_keys = sorted(set.union(set(node1), set(node2)))
    deleted_keys = set(node1).difference(set(node2))
    added_keys = set(node2).difference(set(node1))
    changed_keys = set(node1).intersection(set(node2))

    return dict(map(get_difference, all_keys))


def generate_diff(pathfile1, pathfile2):

    data1, data2 = get_data(pathfile1), get_data(pathfile2)

    if (data1 is False) or (data2 is False):
        return 'ERROR_MESSAGE'

    diff_dict = make_diff(data1, data2)

    return diff_dict


pathfile1 = '/Users/pavelminaev/python-project-lvl2/tests/fixtures/tree_files/tree1.json'
pathfile2 = '/Users/pavelminaev/python-project-lvl2/tests/fixtures/tree_files/tree2.json'

print(generate_diff(pathfile1, pathfile2))
