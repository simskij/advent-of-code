from pathlib import Path

from itertools import product

path = Path(__file__).parent / "input.txt"


def solve() -> int:
    """Count overlap"""

    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()
    
    vents = []
    for line in lines:
        start, stop = line.split("->")
        vents.append(
          Vent(Coord(start), Coord(stop))
        )

    return (
        count_overlaps(vents, False),
        count_overlaps(vents, True),
    )

def count_overlaps(vents, include_diagonal: bool) -> int:
    matrix = [[0 for y in range(1000)] for x in range(1000)]

    if not include_diagonal:
        vents = filter(
            lambda v: not is_diagonal(v.start, v.stop),
            vents
        )

    for vent in vents:
        x_range, y_range = get_ranges(vent.start, vent.stop)
        operation = zip if is_diagonal(vent.start, vent.stop) else product
        for x, y in operation(x_range, y_range):
            matrix[x][y] += 1

    return sum([len([x for x in y if x >= 2]) for y in matrix])


class Coord:
    def __init__(self, pair: str):
        left, right = pair.split(",")
        self.x = int(right)
        self.y = int(left)


class Vent:
    def __init__(self, start: Coord, stop: Coord):
        self.start = start
        self.stop = stop


def is_diagonal(start: Coord, stop: Coord) -> bool:
    return start.x != stop.x and start.y != stop.y

def get_ranges(start: Coord, stop: Coord):
    x_inc = 1 if start.x <= stop.x else -1
    y_inc = 1 if start.y <= stop.y else -1

    x_vals = range(start.x, stop.x + x_inc, x_inc)
    y_vals = range(start.y, stop.y + y_inc, y_inc)

    return x_vals, y_vals
