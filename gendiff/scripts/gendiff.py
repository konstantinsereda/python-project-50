# from brain_games.games import game_even
# from brain_games.game_launcher import game_launcher
import argparse
import json

parser = argparse.ArgumentParser(add_help=False,
                                 prog='gendiff',
                                 description='Compares two configuration '
                                             'files and shows a difference.',
                                 epilog='epilog')
parser.add_argument('first_file', type=str, help='')
parser.add_argument('second_file', type=str, help='')
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0', help="Show program's version "
                                                 "number and exit.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Show this help message and exit.')
parser.add_argument('-f', '--format', default=argparse.SUPPRESS,
                    help='set format of output')
args = parser.parse_args()


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
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
