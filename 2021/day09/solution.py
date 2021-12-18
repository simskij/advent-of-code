"""Day 9: Smoke Basin"""
from pathlib import Path
import math

path = Path(__file__).parent / "input.txt"
name = "Smoke Basin"
NEIGHBOURS = (0, 1), (0, -1), (1, 0), (-1, 0)


def generate():
    entries = []
    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()
        for line in lines:
            entries.append([int(height) for height in line.strip()[0:]])
    low_points = get_low_points(entries)
    return [entries, low_points]


def get_low_points(board):
    low_points = []
    for y, row in enumerate(board):
        for x, point in enumerate(row):
            if is_low_point(y, x, board):
                low_points.append([y, x])
    return low_points


def is_low_point(y, x, rows):
    point = rows[y][x]
    for ax, ay in NEIGHBOURS:
        if y+ay < 0 or x+ax < 0:
            continue
        if y+ay >= len(rows) or x+ax >= len(rows[y]):
            continue
        if rows[y+ay][x+ax] <= point:
            return False

    return True


def part_1(data):
    board, low_points = data
    risks = [ (board[p[0]][p[1]] + 1) for p in low_points]
    return str(sum(risks))


def part_2(data):
    rows, low_points = data
    seen = set()
    sizes = []
    candidates = []
    for y, x in low_points:
        if (y, x) in seen:
            continue
        seen.add((y, x))
        candidates.append([y, x])
        size = 0
        while candidates:
            size += 1
            y, x = candidates.pop()

            for ay, ax in NEIGHBOURS:
                if y + ay < 0 or y + ay >= len(rows):
                    continue
                if x + ax < 0 or x + ax >= len(rows[y]):
                    continue
                if rows[y+ay][x+ax] == 9:
                    continue
                if rows[y+ay][x+ax] <= rows[y][x]:
                    continue
                if (y+ay, x+ax) in seen:
                    continue

                candidates.append([y+ay, x+ax])
                seen.add((y+ay, x+ax))
        sizes.append(size)
    return str(math.prod(sorted(sizes, reverse=True)[:3]))
