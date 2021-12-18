from pathlib import Path


path = Path(__file__).parent / "input.txt"
name = "Binary Diagnostic"


def generate():
    with open(path, "r") as file_input:
        return file_input.readlines()

def part_1(lines) -> str:
    entries = [0] * len(lines[0].strip())
    for line in lines:
        line = line.strip()
        for i, bit in enumerate(int(bit) for bit in line):
            entries[i] += 1 if bit == 1 else -1

    gamma = ""
    epsilon = ""
    for digit in entries:
        gamma += "1" if digit > 0 else "0"
        epsilon += "1" if digit < 0 else "0"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return str(gamma * epsilon)


def part_2(lines_in) -> int:
    oxygen = 0
    pos = 0
    oxygen_lines = lines_in
    carbon_lines = lines_in
    while pos < 12:

        if len(oxygen_lines) > 1:
            total = sum([(1 if digits[pos] == '1' else -1) for digits in oxygen_lines])
            oxygen_filter = 1 if total >= 0 else 0
            oxygen_lines = [line for line in oxygen_lines if line[pos] == str(oxygen_filter)]

        if len(carbon_lines) > 1:
            total = sum([(1 if digits[pos] == '1' else -1) for digits in carbon_lines])
            carbon_filter = 0 if total >= 0 else 1
            carbon_lines = [line for line in carbon_lines if line[pos] == str(carbon_filter)]

        pos += 1

    oxygen = int(oxygen_lines[0], 2)
    carbon = int(carbon_lines[0], 2)
    return str(oxygen * carbon)


