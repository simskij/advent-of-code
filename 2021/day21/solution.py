from scipy.spatial.transform import Rotation as R
import numpy as np
import itertools
import functools
from copy import deepcopy
from pathlib import Path

path = Path(__file__).parent / "input.txt"
name = "Dirac Dice"

def generate(do_print=False) -> (int, int):
    return [6, 1]


class Die:
    def __init__(self, sides):
        self.last_roll = 0
        self.sides = sides

    def roll(self):
        self.last_roll = (self.last_roll - 1) % self.sides + 2
        return self.last_roll

def part_1(positions):
    positions = deepcopy(positions)
    rolls = 0
    scores = [0, 0]
    player = 0
    die = Die(100)
    while True:
        rolls += 3
        throws = [die.roll() for _ in range(3)]
        positions[player] = 1 + ((positions[player] + sum(throws) - 1) % 10)
        scores[player] += positions[player]
        if any(score >= 1000 for score in scores):
            return str(rolls * (scores[(player + 1) % 2]))
        player = int(not player)
    return str(0)


class DiracDie:

    def __init__(self):
        self.counts = 0
        self.winners = []
        self.throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]
        print(self.throws)

    @functools.lru_cache(maxsize=None)
    def play(self, a_pos, a_score, b_pos, b_score, current):
        pos = a_pos if current == 0 else b_pos
        positions = [(pos + throw - 1) % 10 + 1 for throw in self.throws]
        self.counts += 1
        if a_score >= 21:
            return 1, 0
        if b_score >= 21:
            return 0, 1
        if current == 0:
            matches = [
                self.play(new_p, a_score + new_p, b_pos, b_score, 1)
                for new_p in positions
            ]
        else:
            matches = [
                self.play(a_pos, a_score, new_p, b_score + new_p, 0)
                for new_p in positions
            ]
        return sum(a for a, _ in matches), sum(b for _, b in matches)

def part_2(positions):
    a_pos, b_pos = deepcopy(positions)
    dirac = DiracDie()
    print(positions[0], positions[1])
    res = dirac.play(a_pos, 0, b_pos, 0, 0)
    return str(max(res))
