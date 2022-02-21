from pathlib import Path
from functools import reduce

path = Path(__file__).parent / "input.txt"
name = "Trick Shot"


def generate(do_print=False) -> (int, int):

    with open(path, "r", encoding="utf-8") as file_input:
        return [[int(node) for node in line.strip()] for line in file_input.readlines()]


max_y = -1

bounds_y = [-100, 500]

max_y = 10 ** 100

def part_1(grid):
    return str(solve(grid)[0])


def part_2(grid):
    return str(solve(grid)[1])


def solve(grid):
    target_y = [-215, -186]
    target_x = [34, 67]
    max_y = 0
    total = 0
    for x in range(0, 100):
        for y in range(-500, 500):
            cur_y = 0
            cur_x = 0
            vx = x
            vy = y
            current_max_y = 0
            while -500 <= cur_y <= 100000:
                cur_y += vy
                cur_x += vx
                current_max_y = max(current_max_y, cur_y)
                if vx > 0:
                    vx -= 1

                vy -= 1

                if target_y[0] <= cur_y <= target_y[1] and target_x[0] <= cur_x <= target_x[1]:
                    total += 1
                    max_y = max(current_max_y, max_y)
                    break
    return max_y, total
