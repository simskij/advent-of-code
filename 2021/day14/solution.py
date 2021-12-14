"""Day 14: Extended Polymerization"""

from pathlib import Path
from collections import defaultdict


path = Path(__file__).parent / "input.txt"


def solve(do_print=False) -> (int, int):
    """Day 14: Extended Polymerization"""

    silver = 0
    gold = 0

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

    for i in range(1, 41):
        new_counts = defaultdict(int)
        for pair, count in counts.items():

            inj = pairs[pair]
            left = pair[0] + inj
            right = inj + pair[1]

            singles[inj] += count
            new_counts[left] += count
            new_counts[right] += count

        if i == 10:
            silver = max(singles.values()) - min(singles.values())

        counts = new_counts

    gold = max(singles.values()) - min(singles.values())

    return silver, gold
