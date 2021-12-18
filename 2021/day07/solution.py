"""Calculate fuel consumption to align crabs"""
from pathlib import Path


path = Path(__file__).parent / "input.txt"
name = "The Treachery of Whales"


def generate():
    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()
        positions = [int(line) for line in lines[0].split(',')]

    return positions


def part_1(positions) -> str:
    return str(solve(positions))


def part_2(positions) -> str:
    return str(solve(positions, True))


def solve(positions, gold: bool = False) -> int:
    """Calculate fuel consumption to align crabs"""
    totals = []
    for i in range(max(positions)):
        total = 0
        for crab in positions:
            distance = abs(crab - i)
            # doable using sum(range(distance), but at a much
            # higher cost than just calculating the triangular number
            if gold:
                total += distance * (distance + 1) // 2
            else:
                total += abs(crab - i)
        totals.append(total)
    return min(totals)
