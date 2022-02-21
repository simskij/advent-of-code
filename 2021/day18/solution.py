from pathlib import Path
from copy import deepcopy
import json
import itertools
import math

path = Path(__file__).parent / "input.txt"
name = "Snailfish"


class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = None
        self.left = None
        self.right = None

        if type(value) == list:
            self.left = Node(self, value[0])
            self.right = Node(self, value[1])
        if type(value) == int:
            self.value = value

    def reduce(self):
        while True:
            root = self.root
            if exploding := root.get_exploding():
                exploding.explode()
                continue
            if splitting := root.get_splitting():
                splitting.split()
                continue
            break

    def get_exploding(self):
        queue = [(self.root, 0)]
        while queue:
            current, depth = queue.pop()
            if not current.left and not current.right:
                continue
            if depth >= 4:
                return current
            queue.append((current.right, depth+1))
            queue.append((current.left, depth+1))

    def get_splitting(self):
        queue = [self.root]
        while queue:
            current = queue.pop()
            if current.value and current.value >= 10:
                return current
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)

    def add(self, val):
        self.parent = Node(None, None)
        self.parent.left = self
        self.parent.right = val
        val.parent = self.parent
        return self.parent

    def print_top(self):
        parent = self
        while parent.parent:
            parent = parent.parent
        print(parent)

    @property
    def root(self):
        parent = self
        while parent.parent:
            parent = parent.parent
        return parent

    def split(self):
        val = self.value // 2
        self.left = Node(self, val)
        self.right = Node(self, self.value - val)
        self.value = None

    def find_left(self):
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.find_left()

        node = self.parent.left
        while node.right is not None:
            node = node.right
        return node

    def find_right(self):
        if self.parent is None:
            return None
        if self == self.parent.right:
            return self.parent.find_right()

        node = self.parent.right
        while node.left is not None:
            node = node.left
        return node

    def magnitude(self):
        if self.value is not None:
            return self.value

        left = self.left.magnitude()
        right = self.right.magnitude()

        return left*3 + right*2

    def explode(self):
        leftie = self.find_left()
        if leftie:
            leftie.value += self.left.value

        rightie = self.find_right()
        if rightie and self.right.value:
            rightie.value += self.right.value

        self.value = 0
        self.left = None
        self.right = None


def generate(do_print=False) -> (int, int):

    with open(path, "r", encoding="utf-8") as file_input:
        return [line.strip() for line in file_input.readlines()]


def build_node_tree(line):
    return Node(None, json.loads(line))


def part_1(lines):
    node = Node(None, json.loads(lines[0]))
    for line in lines[1:]:
        node.add(Node(None, json.loads(line)))
        node = node.root
        node.reduce()
    return str(node.magnitude())


def part_2(lines):
    max_magnitude = 0
    nodes = [Node(None, json.loads(line)) for line in lines]
    for left, right in list(itertools.product(nodes, nodes)):
        if left == right:
            continue
        left = deepcopy(left)
        right = deepcopy(right)
        left.add(right)
        left.root.reduce()
        max_magnitude = max(max_magnitude, left.root.magnitude())

    return str(max_magnitude)

