from pathlib import Path


path = Path(__file__).parent / "input.txt"


def solve():
    entries = []
    with open(path, "r") as file_input:
        entries = file_input.readlines()

        for i, entry in enumerate(entries):
            entries[i] = int(entry.strip())

    solution_1 = part_1(entries)
    solution_2 = part_2(entries)
    return solution_1, solution_2


def part_1(entries) -> str:
    last = entries[0]
    increases = 0
    for entry in entries[1:]:
        if entry > last:
            increases += 1
        last = entry
    return str(increases)


def part_2(entries) -> str:
    last = entries[0] + entries[1] + entries[2]
    increases = 0
    for i, _ in enumerate(entries[1:]): 
        if i+2 >= len(entries):
            break
        window = entries[i] + entries[i+1] + entries[i+2]
        if window > last:
            increases += 1
        last = window
    return str(increases)
