"""Day 14: Extended Polymerization"""

from pathlib import Path
from functools import reduce

path = Path(__file__).parent / "input.txt"


def solve(do_print=False) -> (int, int):
    """Day 14: Extended Polymerization"""

    with open(path, "r", encoding="utf-8") as file_input:
        lines = [line.strip() for line in file_input.readlines()]

    return 0, 0
