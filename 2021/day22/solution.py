from copy import deepcopy
from pathlib import Path
from collections import Counter
import sqlite3

path = Path(__file__).parent / "input.txt"
name = "Reactor Reboot"


class Instruction:
    def __init__(self, x, y, z, state):
        self.x = x
        self.y = y
        self.z = z
        self.state = state

    def cube(self):
        return (self.x, self.y, self.z)

    def inside(self, limits):
        positions = self.x + self.y + self.z
        return all(
            p >= limits[0] and p <= limits[1]
            for p in positions
        )


def generate(do_print=False) -> (int, int):
    instructions = list()
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        state, coords = line.split(" ")

        x, y, z = coords.split(",")
        x_start, x_end = x[2:].split("..")
        y_start, y_end = y[2:].split("..")
        z_start, z_end = z[2:].split("..")

        instructions.append(
            Instruction(
                (int(x_start), int(x_end)),
                (int(y_start), int(y_end)),
                (int(z_start), int(z_end)),
                state == "on"
            )
        )
    return instructions


def part_1(data):
    return solve([
        item for item in data
        if item.inside([-50, 50])
    ])


def part_2(data):
    return solve(data)


def get_intersection(left, right):
    x_start = max(left[0][0], right[0][0])
    x_end = min(left[0][1], right[0][1])

    if x_start > x_end:
        return

    y_start = max(left[1][0], right[1][0])
    y_end = min(left[1][1], right[1][1])

    if y_start > y_end:
        return

    z_start = max(left[2][0], right[2][0])
    z_end = min(left[2][1], right[2][1])

    if z_start > z_end:
        return

    return ((x_start, x_end), (y_start, y_end), (z_start, z_end))


def get_area(cube):
    x, y, z = cube
    return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)


def solve(instructions):
    cubes = Counter()
    for instruction in instructions:
        changes = Counter()
        if instruction.state == 1:
            changes[instruction.cube()] = 1
        for cube, state in cubes.items():
            if intersection := get_intersection(instruction.cube(), cube):
                changes[intersection] -= state
        cubes.update(changes)

    return str(sum(
        get_area(cube) * state
        for cube, state in cubes.items()
    ))
