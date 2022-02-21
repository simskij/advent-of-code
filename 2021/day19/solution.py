from scipy.spatial.transform import Rotation as R
import numpy as np
from pathlib import Path
from itertools import combinations

path = Path(__file__).parent / "input.txt"
name = "Beacon Scanner"


class Scanner:
    def __init__(self, points):
        self.points = frozenset(points)
        self.rotations = self.get_rotations()
        self.position = (0, 0, 0)

    def get_rotations(self):
        rotations = [
            lambda x, y, z: ((-y, x, z), (-x, -y, z), (y, -x, z)),
            lambda x, y, z: ((z, y, -x), (-x, y, -z), (-z, y, x)),
            lambda x, y, z: ((x, -z, y), (x, -y, -z), (x, z, -y)),
        ]
        all_points = {self.points}
        for rotate in rotations:
            rotated_points = set()
            for points in all_points:
                rotated = set(zip(*(rotate(*point) for point in points)))
                rotated_points = rotated_points.union(rotated)
            all_points = all_points.union(rotated_points)
        return all_points

    def match(self, scanner):
        for rotation in scanner.rotations:
            for px, py, pz in self.points:
                for rx, ry, rz in rotation:
                    dx, dy, dz = px - rx, py - ry, pz - rz
                    cloud = set((x + dx, y + dy, z + dz) for x, y, z in rotation)
                    if len(self.points & cloud) >= 12:
                        return cloud, (dx, dy, dz)
        return None, None


def generate(do_print=False) -> (int, int):
    with open(path, "r", encoding="utf-8") as file:
        data = file.read().strip().split('\n\n')

    scanners = []
    for line in data:
        points = set()
        scans = line.split("\n")[1:]
        for scan in scans:
            point = tuple(int(x) for x in scan.split(","))
            points.add(point)

        scanners.append(Scanner(points))

    return scanners


def part_1(scanners):
    points = scanners[0].points
    to_match = scanners[1:]
    anchors = [scanners[0]]
    while anchors:
        anchor = anchors.pop()
        match_needed = []
        for scanner in to_match:
            abs_points, position = anchor.match(scanner)
            if abs_points is not None:
                points |= abs_points
                scanner.points = abs_points
                anchors.append(scanner)
                scanner.position = position
            else:
                match_needed.append(scanner)
        to_match = match_needed
    return str(len(points))


def part_2(scanners):
    part_1(scanners)

    dist = 0
    scanner_positions = {scanner.position for scanner in scanners}
    for (x1, y1, z1), (x2, y2, z2) in combinations(scanner_positions, 2):
        dist = max(dist, abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))
    return str(dist)

