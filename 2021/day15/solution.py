from pathlib import Path
from functools import reduce

path = Path(__file__).parent / "input.txt"
name = "Chiton"

NEIGHBOURS = (
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
)

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return f"{self.position[0]}:{self.position[1]}"

def generate(do_print=False) -> (int, int):

    with open(path, "r", encoding="utf-8") as file_input:
        return [[int(node) for node in line.strip()] for line in file_input.readlines()]


def part_1(grid):
    solver = Solver(grid)
    return str(solver.search())


def part_2(grid):
    solver = Solver(grid, True)
    return str(solver.search())


class Solver:
    def __init__(self, grid, wrapping=False):
        self._grid = grid
        self._wrapping = wrapping

    def search(self):
        start = (0, 0)
        if self._wrapping:
            goal = (self.width * 5 - 1, self.height * 5 - 1)
        else:
            goal = (self.width - 1, self.height - 1)
        frontier = [[start]]
        parents = {}
        cost = {}

        parents[start] = None
        cost[start] = 0

        while True:
            i = 0
            while True:
                if not frontier[i]:
                    i += 1
                else:
                    y, x = current = frontier[i].pop(0)
                    break
            if current == goal:
                break
            for n in self.get_neighbours(y, x):
                n_cost = cost[current] + self.get_cost(n[0], n[1])
                if n not in cost or n_cost < cost[n]:
                    cost[n] = n_cost
                    while len(frontier) <= n_cost:
                        frontier += [[]]
                    frontier[n_cost] += [n]
                    parents[n] = current
        return cost[goal]


    def get_cost(self, y, x, ext=False):
        cost = self._grid[y % self.width][x % self.height]
        if self._wrapping:
            cost = (cost + x // self.width + y // self.height - 1) % 9 + 1
        return cost

    def get_neighbours(self, y, x):
        neighbours = []
        width = self.width if not self._wrapping else self.width * 5
        height = self.width if not self._wrapping else self.height * 5
        for my, mx in NEIGHBOURS:
            nx, ny = x + mx, y + my
            if nx < 0 or nx >= width:
                continue
            if ny < 0 or ny >= height:
                continue
            neighbours.append((ny, nx))
        return neighbours

    @property
    def width(self):
        return len(self._grid[0])

    @property
    def height(self):
        return len(self._grid)

