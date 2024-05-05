import pytest
import filecmp
from gendiff.scripts.gendiff import generate_diff

def test_flat_json():
    # with pytest.raises(ValueError) as error:
    #     error(int(1))ё
    file_output = open('/Users/konst/Hexlet/python-project-50/tests/fixtures/output.txt', 'w')
    file_output.write(generate_diff('/Users/konst/Hexlet/python-project-50/tests/fixtures/file1.json',
                           '/Users/konst/Hexlet/python-project-50/tests/fixtures/file2.json'))
    file_output.close()

    result_testing_func = '/Users/konst/Hexlet/python-project-50/tests/fixtures/output.txt'
    correct_output = '/Users/konst/Hexlet/python-project-50/tests/fixtures/correct_output'
    assert filecmp.cmp(result_testing_func, correct_output)


# можем использовать библиотеку pytest вместе с модулем filecmp для сравнения файлов.
#
#
# import filecmp
# from your_module import generate_diff
#
#
# def test_generate_diff():
#     # Вызываем функцию generate_diff() и сохраняем результат во временный файл
#     temp_output_file = 'temp_output.txt'
#     generate_diff('path/to/input_file1', 'path/to/input_file2', output=temp_output_file)
#
#     # Сравниваем временный файл с файлом содержимого 'fixtures/correct_output'
#     assert filecmp.cmp(temp_output_file, 'fixtures/correct_output')