from gendiff.cli import parse
import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff = []
    for key in keys:
        if key not in data1:
            diff.append(f'+ {key}: {data2[key]}')
        elif key not in data2:
            diff.append(f'- {key}: {data1[key]}')
        elif data1[key] != data2[key]:
            diff.append(f'- {key}: {data1[key]}')
            diff.append(f'+ {key}: {data2[key]}')
        elif data1[key] == data2[key]:
            diff.append(f'  {key}: {data1[key]}')

    return '{\n  ' + '\n  '.join(diff) + '\n}'


def main():
    args = parse()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
