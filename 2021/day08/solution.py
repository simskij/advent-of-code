"""Day 8: Seven Segment Search"""
from pathlib import Path


path = Path(__file__).parent / "input.txt"
name = "Seven Segment Search"


def generate():
    """Day 8: Seven Segment Search"""

    entries = []
    with open(path, "r", encoding="utf-8") as file_input:
        lines = file_input.readlines()
        for line in lines:
            wires, segments = (
                    parts.strip().split(" ")
                    for parts
                    in line.split(" | ")
                )
            entries.append([wires, segments])

    return entries


def part_1(entries) -> int:
    silver = 0
    for _, segments in entries:
        for segment in segments:
            silver += 1 if len(segment) == 2 else 0  # 1
            silver += 1 if len(segment) == 4 else 0  # 4
            silver += 1 if len(segment) == 3 else 0  # 7
            silver += 1 if len(segment) == 7 else 0  # 8
    return str(silver)


def part_2(entries) -> int:
    summed = 0
    for entry in entries:
        result = solve_gold_entry(entry)
        summed += result
    return str(summed)

def solve_gold_entry(entry) -> int:
    entries = entry
    nums: dict[int, str] = {}

    nums[1] = find(lambda x: len(x) == 2, entries[0])
    nums[4] = find(lambda x: len(x) == 4, entries[0])
    nums[7] = find(lambda x: len(x) == 3, entries[0])
    nums[8] = find(lambda x: len(x) == 7, entries[0])
    nums[3] = find(lambda x: len(x) == 5 and contains(x, nums[1]), entries[0])
    nums[9] = "".join(set(f"{nums[4]}{nums[3]}"))

    nums[0] = find(
        (
            lambda x: len(x) == 6
            and contains(x, nums[1])
            and not contains(x, nums[9])
        ),
        entries[0]
    )

    nums[2] = find(
        (
            lambda x: len(x) == 5
            and list(set(nums[8]) - set(nums[9]))[0] in x
        ),
        entries[0]
    )

    nums[5] = find(
        (
            lambda x: len(x) == 5
            and x != nums[2]
            and x != nums[3]
        ),
        entries[0]
    )
    nums[6] = find(
        (
            lambda x: len(x) == 6
            and contains(x, nums[5])
            and sorted(x) != sorted(nums[9])
        ),
        entries[0]
    )

    for i, value in nums.items():
        for j, item in enumerate(entries[1]):
            if sorted(value) == sorted(item):
                entries[1][j] = str(i)

    return int(''.join([str(i) for i in entries[1]]))


def contains(left, right) -> bool:
    """Checks if left contains letters of right regardless of order"""
    return all(letter in list(left) for letter in list(right))


def find(pred, iterable):
    """Returns first item in list that matches `pred`"""
    for element in iterable:
        if pred(element):
            return element
