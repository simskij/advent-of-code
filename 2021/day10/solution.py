"""Day 10: Syntax Scoring"""
from pathlib import Path
import math

path = Path(__file__).parent / "input.txt"
name = "Syntax Scoring"

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


def generate():
    with open(path, "r", encoding="utf-8") as file_input:
        return [line.strip() for line in file_input.readlines()]


def part_1(lines):
    score = 0
    for line in lines:
        expected = []
        for char in line:
            if char in "([{<":
                expected.append(matching[char])
            elif char in ")]}>":
                if char != expected.pop():
                    score += silver_points[char]
    return str(score)


def part_2(lines):
    incomplete = []
    for line in lines:
        expected = []
        corrupt = False
        for char in line:

            if char in "([{<":
                expected.append(matching[char])
            elif char in ")]}>":
                if char != expected.pop():
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
    return str(sorted(scores)[middle])
