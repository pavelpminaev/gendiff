import pytest
from gendiff.parsing import parsing_data


@pytest.mark.parametrize('data_file', ['tests/fixtures/flat_files//tree1.json',
                                       'tests/fixtures/flat_files/tree1.yml',
                                       'tests/fixtures/flat_files/tree1.yaml'])
def test_parsing(data_file):
    dict_data = parsing_data(open(data_file), data_file)
    assert isinstance(dict_data, dict)
