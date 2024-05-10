from gendiff.cli import parse
from gendiff.file_parcer import get_data


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

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
