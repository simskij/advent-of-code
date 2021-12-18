"""Day 11: Syntax Scoring"""
from pathlib import Path
import math

from matplotlib import pyplot as plt
from matplotlib import animation
from os.path import expanduser

path = Path(__file__).parent / "input.txt"
name = "Dumbo Octopus"

NEIGHBOURS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
)

animate = False

def generate():
    board = []

    with open(path, "r", encoding="utf-8") as file_input:
        lines = [line.strip() for line in file_input.readlines()]
        board = [[int(octopus) for octopus in line] for line in lines]

    height = len(board)
    width = len(board[0])

    return [board, height, width]


def part_1(data):
    board, height, width = data
    return str(solve(board, height, width))


def part_2(data):
    board, height, width = data
    return str(solve(board, height, width, True))


def solve(board, height, width, untilSyncing: bool = False):
    states = []
    step = 0
    total = 0
    while True:
        step += 1
        flashed = []
        flashing = []
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                board[y][x] += 1
                if col >= 9:
                    flashing.append([y, x])

        while flashing:
            y, x = flashing.pop()
            flashed.append([y, x])
            board[y][x] = 0

            for vertical, horizontal in NEIGHBOURS:
                adjacent_y = y+vertical
                adjacent_x = x+horizontal

                if adjacent_y < 0 or adjacent_y >= height:
                    continue
                if adjacent_x < 0 or adjacent_x >= width:
                    continue

                if [adjacent_y, adjacent_x] in flashed:
                    continue
                if [adjacent_y, adjacent_x] in flashing:
                    continue

                board[adjacent_y][adjacent_x] += 1

                if board[adjacent_y][adjacent_x] > 9:
                    flashing.append([adjacent_y, adjacent_x])
        if animate:
            states.append([[col for col in row] for row in board])
        if step <= 100:
            total += len(flashed)
        elif not untilSyncing:
            return total
        elif len(flashed) == height * width:
            if animate:
                animate_states(states)
            return step




def animate_states(states):
    fig = plt.figure()
    im = plt.imshow(states[0], animated=True, cmap="copper")

    def animation_func(frame):
        im.set_array(frame)
        return im

    anim = animation.FuncAnimation(
            fig,
            animation_func,
            blit=True,
            interval=100,
            frames=states
    )
    anim.save(f"{expanduser('~')}/day-11-animation.mp4")

