"""Day 14: Extended Polymerization"""

from pathlib import Path
from collections import defaultdict


path = Path(__file__).parent / "input.txt"
name = "Extended Polymerization"


def generate():
    with open(path, "r", encoding="utf-8") as file_input:
        lines = [line.strip() for line in file_input.readlines()]

    sequence = lines[0]
    pairs = dict(line.split(" -> ") for line in lines[2:])

    counts = defaultdict(int)
    singles = defaultdict(int)

    for i, _ in enumerate(sequence):
        singles[sequence[i]] += 1
        if i == 0:
            continue
        counts[sequence[i-1:i+1]] += 1
    return [pairs, counts, singles]


def part_1(data):
    pairs, counts, singles = data
    return str(solve(pairs.copy(), counts.copy(), singles.copy(), 10))


def part_2(data):
    pairs, counts, singles = data
    return str(solve(pairs.copy(), counts.copy(), singles.copy(), 40))


def solve(pairs, counts, singles, limit):
    for i in range(1, (limit + 1)):
        new_counts = defaultdict(int)
        for pair, count in counts.items():

            inj = pairs[pair]
            left = pair[0] + inj
            right = inj + pair[1]

            singles[inj] += count
            new_counts[left] += count
            new_counts[right] += count
        counts = new_counts
    return max(singles.values()) - min(singles.values())
