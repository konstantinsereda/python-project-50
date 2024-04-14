# from brain_games.games import game_even
# from brain_games.game_launcher import game_launcher
import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0', help="Show program's version number and exit.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Show this help message and exit.')
args = parser.parse_args()

def main():
    pass


if __name__ == "__main__":
    main()
