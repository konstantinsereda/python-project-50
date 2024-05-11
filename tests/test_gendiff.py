import json
import yaml
import pytest
import sys
import filecmp
from gendiff.cli import parse
from gendiff.scripts.gendiff import main
from gendiff.scripts.gendiff import generate_diff
from unittest.mock import patch
from gendiff.file_parcer import get_data


def test_get_data():
    pass


def test_flat_json():
    data1 = get_data('tests/fixtures/file1.json')
    data2 = get_data('tests/fixtures/file2.json')
    file_output = open('tests/fixtures/output.txt', 'w')
    diff = generate_diff(data1, data2)
    file_output.write('{\n  ' + '\n  '.join(diff) + '\n}')
    file_output.close()
    result_testing_func = 'tests/fixtures/output.txt'
    correct_output = 'tests/fixtures/correct_output'
    assert filecmp.cmp(result_testing_func, correct_output)


def test_cascaded_json():
    data1 = get_data('tests/fixtures/file_cascaded1.json')
    data2 = get_data('tests/fixtures/file_cascaded2.json')
    file_output = open('tests/fixtures/output.txt', 'w')
    diff = generate_diff(data1, data2)
    file_output.write(json.dumps(diff, indent=4))
    file_output.close()
    result_testing_func = 'tests/fixtures/output.txt'
    correct_output = 'tests/fixtures/correct_output_cascaded'
    assert filecmp.cmp(result_testing_func, correct_output)


def test_flat_yaml():
    data1 = get_data('tests/fixtures/file1.yaml')
    data2 = get_data('tests/fixtures/file2.yaml')
    file_output = open('tests/fixtures/output.txt', 'w')
    diff = generate_diff(data1, data2)
    file_output.write('{\n  ' + '\n  '.join(diff) + '\n}')
    file_output.close()
    result_testing_func = 'tests/fixtures/output.txt'
    correct_output = 'tests/fixtures/correct_output'
    assert filecmp.cmp(result_testing_func, correct_output)


def test_cli():
    paths = parse(['tests/fixtures/file1.json', 'tests/fixtures/file2.json'])
    assert paths.first_file == 'tests/fixtures/file1.json'
    assert paths.second_file == 'tests/fixtures/file2.json'
#    assert paths.format == 'stylish'
