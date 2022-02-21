from halo import Halo

import argparse
import time

import day01.solution as day01
import day02.solution as day02
import day03.solution as day03
import day04.solution as day04
import day05.solution as day05
import day06.solution as day06
import day07.solution as day07
import day08.solution as day08
import day09.solution as day09
import day10.solution as day10
import day11.solution as day11
import day12.solution as day12
import day13.solution as day13
import day14.solution as day14
import day15.solution as day15
import day16.solution as day16
import day17.solution as day17
import day18.solution as day18
import day19.solution as day19
import day21.solution as day21
import day22.solution as day22
import day23.solution as day23

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
            usage="%(prog)s [OPTION]...",
            description="Solve either all days or a particular one"
    )
    parser.add_argument('-d', '--day', type=int)
    return parser


def main():
    parser = init_argparse()
    args = parser.parse_args()

    switcher = {
        1: day01,
        2: day02,
        3: day03,
        4: day04,
        5: day05,
        6: day06,
        7: day07,
        8: day08,
        9: day09,
        10: day10,
        11: day11,
        12: day12,
        13: day13,
        14: day14,
        15: day15,
        16: day16,
        17: day17,
        18: day18,
        19: day19,
        21: day21,
        22: day22,
        23: day23,
    }

    if args.day:
        day = switcher.get(args.day)
        filtered = {}
        filtered[args.day] = day
        switcher = filtered
    spinner = Halo(text="Running solvers...", spinner="dots")
    spinner.start()

    output = []
    for day in switcher:
        def get_diff(start, end):
            return f"{(end - start) // 1_000} μs"
        solver = switcher.get(day)
        start = time.time_ns()
        data = solver.generate()
        after_gen = get_diff(start, time.time_ns())

        start = time.time_ns()
        silver = switcher.get(day).part_1(data)
        after_silver = get_diff(start, time.time_ns())


        start = time.time_ns()
        gold = switcher.get(day).part_2(data)
        after_gold = get_diff(start, time.time_ns())

        # day = f"🎁 Day {day}: {switcher.get(day).name}"
        g = f"⚡ {after_gen.rjust(10)}"
        a = f"🥈 {silver.ljust(20)} {after_silver.rjust(10)}"
        b = f"🥇 {gold.ljust(20)} {after_gold.rjust(15)}"
        # output.append(f"{day}\n\n{g}{a}\n{' '*13}{b}\n{divider}")
        output.append(f"🎁 {str(day).zfill(2)} - {solver.name.ljust(30)} {g} {a} {b}")
    spinner.succeed("Solvers completed")
    print("\n" + ('\n'.join(output)))
    return

if __name__ == "__main__":
    main()
