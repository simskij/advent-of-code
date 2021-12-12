"""Day 12: Passage Pathing"""
from pathlib import Path

path = Path(__file__).parent / "input.txt"


def solve() -> (int, int):
    """Day 12: Passage Pathing"""

    with open(path, "r", encoding="utf-8") as file_input:
        lines = [line.strip() for line in file_input.readlines()]

    rooms = dict()
    for line in lines:
        left, right = line.split("-")

        if left not in rooms:
            rooms[left] = [right]
        elif right not in rooms[left]:
            rooms[left].append(right)

        if right not in rooms:
            rooms[right] = [left]
        elif left not in rooms[right]:
            rooms[right].append(left)

    return (
        travel("start", [], rooms),
        travel("start", [], rooms, True)
    )


def travel(current, visited, rooms, allow_twice=False) -> int:
    total = 0
    for option in rooms[current]:
        if option == "start":
            continue
        elif option == "end":
            total += 1
        elif option not in visited or option.isupper():
            total += travel(option, visited + [current], rooms, allow_twice)
        elif not option.isupper() and allow_twice:
            total += travel(option, visited + [current], rooms, False)
    return total
