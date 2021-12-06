"""Calculate fish population after N days"""
from pathlib import Path
from collections import defaultdict
import numpy as np


path = Path(__file__).parent / "input.txt"


def solve() -> int:
    """Calculate the amount of fishes after 80 days"""

    silver = 0
    gold = 0

    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()
        states: dict[int, int] = defaultdict(lambda: 0)
        for entry in lines[0].split(','):
            states[int(entry)] += 1

    for day in range(1, 257):
        newborn = states[0]
        for i in range(0, 8):
            states[i] = states[i+1]
        states[6] += newborn
        states[8] = newborn
        if day == 80:
            silver = sum(states.values())
    gold = sum(states.values())
    return silver, gold
