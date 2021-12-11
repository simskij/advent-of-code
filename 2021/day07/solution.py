"""Calculate fuel consumption to align crabs"""
from pathlib import Path


path = Path(__file__).parent / "input.txt"


def solve() -> int:
    """Calculate fuel consumption to align crabs"""

    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()
        positions = [int(line) for line in lines[0].split(',')]

    silver_totals = []
    gold_totals = []
    for i in range(max(positions)):
        silver_total = 0
        gold_total = 0
        for crab in positions:
            distance = abs(crab - i)
            # doable using sum(range(distance), but at a much
            # higher cost than just calculating the triangular number
            gold_total += distance * (distance + 1) // 2
            silver_total += abs(crab - i)
        gold_totals.append(gold_total)
        silver_totals.append(silver_total)
    return min(silver_totals), min(gold_totals)
