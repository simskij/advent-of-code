
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
        1: day01.solve,
        2: day02.solve,
        3: day03.solve,
        4: day04.solve,
        5: day05.solve,
        6: day06.solve,
        7: day07.solve,
        8: day08.solve,
        9: day09.solve,
        10: day10.solve,
        11: day11.solve,
        12: day12.solve,
        13: day13.solve,
        14: day14.solve
    }

    if not args.day:
        print("Running the solvers for all days...\n")
        output = []
        for day in switcher:
            start = time.time_ns()
            silver, gold = switcher.get(day)()

            day = f"🎁 Day {day}".ljust(10)
            a = f"🥈 {silver}".ljust(10)
            b = f"🥇 {gold}".ljust(20)
            t = f"{(time.time_ns() - start) // 1_000} μs".rjust(15)

            output.append(f"{day}{a}{b}{t}")
        print("\n".join(output))
        return

    print(f"Running the solver for day {args.day}...")
    silver, gold = switcher.get(args.day, "Invalid day")()
    print(f"🥈 {silver}\n🥇 {gold}")

    return


if __name__ == "__main__":
    main()
