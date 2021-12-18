from  pathlib import Path


path = Path(__file__).parent / "input.txt"

class Entry:
    def __init__(self, direction: str, distance: int):
        self.direction = direction
        self.distance = distance

name = "Dive!"

def generate():

    entries = []
    with open(path, "r") as file_input:
        lines = file_input.readlines()
        for line in lines:
            segments = line.split()
            entries.append(Entry(segments[0], int(segments[1])))

    return entries


def part_1(entries) -> str:
    depth = 0
    length = 0

    for entry in entries:
        if entry.direction == "forward":
            length += entry.distance
        if entry.direction == "down":
            depth += entry.distance
        if entry.direction == "up":
            depth -= entry.distance

    return str(depth * length)


def part_2(entries) -> str:
    depth = 0
    length = 0
    aim = 0

    for entry in entries:
        if entry.direction == "forward":
            length += entry.distance
            depth += aim * entry.distance
        if entry.direction == "down":
            aim += entry.distance
        if entry.direction == "up":
            aim -= entry.distance

    return str(depth * length)

