import argparse


def parse():
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
    return parser.parse_args()
