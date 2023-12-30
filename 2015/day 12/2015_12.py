import re
import json

INPUT_FILE = r"advent_of_code\2015\day 12\input.txt"


def part1():
    with open(INPUT_FILE) as f:
        string_data = f.read().strip()

    digits = re.findall("(-?\d+)", string_data)
    p1 = sum([int(digit) for digit in digits])
    print(f"Part 1: {p1}")


def part2():
    def sum_numbers_excluding_red(data):
        if isinstance(data, dict):
            if 'red' in data.values():
                return 0
            return sum(sum_numbers_excluding_red(v) for v in data.values())
        elif isinstance(data, list):
            return sum(sum_numbers_excluding_red(v) for v in data)
        elif isinstance(data, (int, float)):
            return data
        else:
            return 0

    with open(INPUT_FILE) as f:
        json_data = json.load(f)

    total_sum_excluding_red = sum_numbers_excluding_red(json_data)
    print(f"Part 2: {total_sum_excluding_red}")


if __name__ == "__main__":
    part1()
    part2()
