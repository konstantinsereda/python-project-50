import pytest
import filecmp
from gendiff.scripts.gendiff import generate_diff

def test_flat_json():
    # with pytest.raises(ValueError) as error:
    #     error(int(1))
    temp_output_file = 'temp_output.txt'
    correct_output = 'fixtures/correct_output'
    # output_generate_diff = main('fixtures/file1.json', 'fixtures/file2.json')
    output_generate_diff = main()
    assert filecmp.cmp(correct_output, output_generate_diff)

# test did not work

def test_generate_diff():
    # Вызываем функцию generate_diff() и сохраняем результат во временный файл
    temp_output_file = 'temp_output.txt'
    generate_diff('path/to/input_file1', 'path/to/input_file2', output=temp_output_file)

    # Сравниваем временный файл с файлом содержимого 'fixtures/correct_output'
    assert filecmp.cmp(temp_output_file, 'fixtures/correct_output')