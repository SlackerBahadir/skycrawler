import click
from rich import print
import sys

from src.find_planets_for_loc import get_planets_for_loc

@click.command()
@click.option('--planets', is_flag=True)
def parser(planets):
    if planets:
        get_planets_for_loc()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(parser.get_help(click.Context(parser)))

    parser()