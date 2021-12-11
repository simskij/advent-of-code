"""Day 10: Syntax Scoring"""
from pathlib import Path
import math

path = Path(__file__).parent / "input.txt"


matching = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

silver_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

gold_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def solve() -> (int, int):
    """Day 10: Syntax Scoring"""

    with open(path, "r", encoding="utf-8") as file_input:
        lines = [line.strip() for line in file_input.readlines()]

    silver_score = 0
    incomplete = []
    for line in lines:
        expected = []
        corrupt = False
        for char in line:

            if char in "([{<":
                expected.append(matching[char])
            elif char in ")]}>":
                if char != expected.pop():
                    silver_score += silver_points[char]
                    corrupt = True
        if not corrupt:
            expected.reverse()
            incomplete.append([line, ''.join(expected)])

    scores = []
    for line, expected in incomplete:
        score = 0
        for char in expected:
            score = score * 5 + gold_points[char]
        scores.append(score)
    middle = math.ceil((len(scores)-1)/2)
    gold_score = sorted(scores)[middle]
    return silver_score, gold_score
