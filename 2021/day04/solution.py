"""Solve day 4"""

from pathlib import Path


path = Path(__file__).parent / "input.txt"


def solve():
    """Solve both parts of day 4"""
    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()

    winner_score = 0

    draws = [int(draw) for draw in lines[0].split(',')]
    boards = get_boards(lines[1:])
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

                score = sum([p for p in board if p != -1]) * int(draw)

                if not winner_score:
                    winner_score = score
                if i not in winners:
                    winners.append(i)
                if len(winners) == len(boards):
                    return winner_score, score

    raise Exception(
        "Could not determine the first and last winner, "
        "likely because of corrupt puzzle input"
    )


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
