from pathlib import Path

import math

path = Path(__file__).parent / "input.txt"
name = "Packet Decoder"


def generate(do_print=False) -> (int, int):
    with open(path, "r", encoding="utf-8") as file_input:
        input = "".join(file_input.readlines()).strip()
        return convert(input)


def part_1(data):
    return str(parse(data)[1])


def part_2(data):
    return str(parse(data)[2])


def convert(data):
    return "".join([
        bin(int(char, 16))[2:].zfill(4)
        for char in data
    ])


def parse(data):
    version = int(data[:3], 2)
    type_id = int(data[3:6], 2)
    versions = version
    data = data[6:]
    totals = []

    if type_id == 4:
        data, total = parse_literal(data)
        totals.append(total)
    else:
        data, version, total = parse_operator(data)
        versions += version
        totals += total

    return (
        data,
        versions,
        calculate(type_id, totals)
    )


def parse_literal(data):
    content = ""
    while True:
        again = data[0] == "1"
        content += data[1:5]
        data = data[5:]
        if not again:
            break
    return data, int(content, 2)


def parse_operator(data):
    totals = []
    length_id = int(data[0])
    data = data[1:]
    versions = 0
    if length_id == 0:
        sub_length = int(data[:15], 2)
        data = data[15:]
        subpackages = data[:sub_length]
        data = data[sub_length:]
        while len(subpackages) > 0:
            subpackages, version, total = parse(subpackages)
            versions += version
            totals.append(total)
    else:
        sub_count = int(data[:11], 2)
        data = data[11:]
        for _ in range(sub_count):
            data, version, total = parse(data)
            totals.append(total)
            versions += version
    return data, versions, totals


def calculate(type_id, values):
    if type_id == 0:
        return sum(values)
    if type_id == 1:
        return math.prod(values)
    if type_id == 2:
        return min(values)
    if type_id == 3:
        return max(values)
    if type_id == 4:
        return values[0]
    if type_id == 5:
        return values[0] > values[1]
    if type_id == 6:
        return values[0] < values[1]
    return values[0] == values[1]
