"""Modul search difference between two collections"""

from gendiff.parsing import get_data
from gendiff.formatters.all_formaters import format_change

ERROR_MESSAGE = "Impossible to build difference. Check your files."


def make_diff(node1, node2):
    def get_difference(key):

        if key in deleted_keys:
            value = {'type': 'deleted', 'value': node1[key]}

        elif key in added_keys:
            value = {'type': 'added', 'value': node2[key]}

        elif key in changed_keys and node1[key] == node2[key]:
            value = {'type': 'unchanged', 'value': node1[key]}

        elif key in changed_keys and node1[key] != node2[key]:
            if isinstance(node1[key], dict) and isinstance(node2[key], dict):
                value = {'type': 'internal_change',
                         'value': make_diff(node1[key], node2[key])}
            else:
                value = {'type': 'changed_value',
                         'value': [node1[key], node2[key]]}

        return key, value

    all_keys = sorted(set.union(set(node1), set(node2)))
    deleted_keys = set(node1).difference(set(node2))
    added_keys = set(node2).difference(set(node1))
    changed_keys = set(node1).intersection(set(node2))

    return dict(map(get_difference, all_keys))


def generate_diff(path_first_file, path_second_file, formatter='stylish'):
    data_of_first_file, data_of_second_file = \
        get_data(path_first_file), get_data(path_second_file)

    if (data_of_first_file is False) or (data_of_second_file is False):
        return ERROR_MESSAGE

    diff_dict = make_diff(data_of_first_file, data_of_second_file)

    format_style = format_change(formatter)

    return format_style(diff_dict)
