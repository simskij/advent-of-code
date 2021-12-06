
import argparse

import day01.solution as day01
import day02.solution as day02
import day03.solution as day03
import day04.solution as day04
import day05.solution as day05
import day06.solution as day06


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
      6: day06.solve
    }

    if not args.day:
        print("Running the solvers for all days...\n")
        for day in switcher:
            silver, gold = switcher.get(day)()
            print(f"Day {day}".ljust(10), f"🥈 {silver}".ljust(10), f"🥇 {gold}")
        return

    print(f"Running the solver for day {args.day}...")
    silver, gold = switcher.get(args.day, "Invalid day")()
    print(f"🥈 {silver}\n🥇 {gold}")

    return


if __name__ == "__main__":
    main()
