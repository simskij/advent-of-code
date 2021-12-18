"""Day 13: Transparent Origami"""
from pathlib import Path
from functools import reduce
from advent_of_code_ocr import convert_6

path = Path(__file__).parent / "input.txt"
name = "Transparent Origami"


def generate():
    folds = []
    coords = []

    with open(path, "r", encoding="utf-8") as file_input:
        lines = [line.strip() for line in file_input.readlines()]

    for line in lines:
        if line == "":
            continue
        if "fold" in line:
            folds.append(line)
        else:
            coords.append([int(coord) for coord in line.split(",")])

    width, height = 1400, 1400
    board = [[False for i in range(width + 1)] for j in range(height+1)]

    for x, y in coords:
        board[y][x] = True

    return [board, folds]


def part_1(data) -> str:
    board, folds = data
    board = fold(board, folds[0])
    summed = sum([sum(row) for row in board])

    return str(summed)


def part_2(data) -> str:
    board, folds = data
    for f in folds:
        board = fold(board, f)

    return read_board(board)


def fold(board, where):
    direction, point = where.split("=")
    point = int(point)

    a = []
    b = []

    if "y" in direction:
        board = board[:point*2+1]
        a = board[:point]
        b = board[point+1:]
        b.reverse()
    else:
        for row in board:
            row = row[:point*2+1]
            a.append(row[:point])
            right = row[point+1:]
            right.reverse()
            b.append(right)

    for y in range(len(a)):
        for x in range(len(a[0])):
            a[y][x] = any([b[y][x], a[y][x]])
    return a


def read_board(board):
    return convert_6(
        "\n".join([
            "".join([
                '.' if dot is False else '#' for dot in line
            ]) for line in board
        ]))

