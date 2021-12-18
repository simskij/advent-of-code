"""Solve day 4"""

from pathlib import Path


path = Path(__file__).parent / "input.txt"
name = "Giant Squid"

def generate():
    """Solve both parts of day 4"""
    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()

    draws = [int(draw) for draw in lines[0].split(',')]
    boards = get_boards(lines[1:])
    return [draws, boards]


def part_1(data) -> str:
    draws, boards = data

    for draw in draws:
        for i, board in enumerate(boards):
            for j, val in enumerate(board):
                if val == int(draw):
                    board[j] = -1

            for j in range(0, 5):
                horizontal = sum(board[j*5:j*5+5])
                vertical = sum(board[j::5])

                if -5 not in [horizontal, vertical]:
                    continue

                return str(sum([p for p in board if p != -1]) * int(draw))


def part_2(data) -> str:
    draws, boards = data
    winners = []

    for draw in draws:
        for i, board in enumerate(boards):
            for j, val in enumerate(board):
                if val == int(draw):
                    board[j] = -1

            for j in range(0, 5):
                horizontal = sum(board[j*5:j*5+5])
                vertical = sum(board[j::5])

                if -5 not in [horizontal, vertical]:
                    continue
                if i not in winners:
                    winners.append(i)
                if len(winners) == len(boards):
                    return str(sum([p for p in board if p != -1]) * int(draw))


def get_boards(lines):
    """Split lines into bingo boards"""
    boards = []
    while len(lines) > 0:
        values = list(
            map(int, ''.join(lines[1:6]).split())
        )
        boards.append(values)
        lines = lines[6:]
    return boards
