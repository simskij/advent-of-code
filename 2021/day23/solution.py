from copy import deepcopy
from pathlib import Path
from collections import Counter
import sqlite3

path = Path(__file__).parent / "input.txt"
name = "Amphipod"


def generate(do_print=False) -> (int, int):
    maze = [
        [None],
        [None],
        [None, 'B', 'A'],
        [None],
        [None, 'C', 'D'],
        [None],
        [None, 'B', 'C'],
        [None],
        [None, 'D', 'A'],
        [None],
        [None]
    ]
    print(maze)
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines


def part_1(data):

    A = ['B', 'A']
    B = ['C', 'D']
    C = ['B', 'C']
    D = ['D', 'A']

    homes = {'A': A, 'B': B, 'C': C, 'D': D}
    costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    return str(0)

def is_done(homes):
    for key, val in homes.items():
        if not all(x == key for x in val):
            return False
    return True

def part_2(data):
    return str(0)
