# import json
from gendiff.cli import parse
from gendiff.file_parcer import get_data


def generate_diff(data1, data2):

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff = []
    for key in keys:
        if key not in data1:
            diff.append(f'+ {key}: {data2[key]}')
        elif key not in data2:
            diff.append(f'- {key}: {data1[key]}')
        elif data1[key] != data2[key]:
            if not isinstance(data1[key], dict) and not isinstance(data2[key], dict):
                diff.append(f'- {key}: {data1[key]}')
                diff.append(f'+ {key}: {data2[key]}')
            else:
                pass
        elif data1[key] == data2[key]:
            diff.append(f'  {key}: {data1[key]}')

#    return '{\n  ' + '\n  '.join(diff) + '\n}'
    return diff


def main():
    args = parse()
    data1 = get_data(args.first_file)
    data2 = get_data(args.second_file)
    diff = generate_diff(data1, data2)
    print(type(diff))
    print(diff)
    result = '{\n  ' + '\n  '.join(diff) + '\n}'
    print(type(result))
    print(result)


if __name__ == '__main__':
    main()
