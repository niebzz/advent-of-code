def push_rocks(row: list[str]) -> list[str]:
    count_O = 0
    for i, item in enumerate(row):
        if item == "O":
            count_O += 1
            row[i] = "."
        elif item == "#" and count_O > 0:
            for j in range(i-count_O, i):
                row[j] = "O"
            count_O = 0

        if i == len(row) - 1 and count_O > 0:
            for k in range(len(row)-count_O, len(row)):
                row[k] = "O"
            count_O = 0
    return row


def transpose_platform_clockwise(data: list[str]) -> list[str]:
    return list(map(lambda x: "".join(reversed(x)), zip(*data)))


def transpose_platform_counterclockwise(data: list[str]) -> list[str]:
    return ["".join(x) for x in reversed(list(zip(*data)))]


def tilt_platform_east(data: list[str]) -> list[str]:
    return ["".join(push_rocks(list(row))) for row in data]


def tilt_platform_west(data: list[str]) -> list[str]:
    return ["".join(reversed(x)) for x in (
        tilt_platform_east(["".join(reversed(x)) for x in data]))]


def tilt_platform_north(data: list[str]) -> list[str]:
    return transpose_platform_counterclockwise(
        tilt_platform_east(transpose_platform_clockwise(data)))


def tilt_platform_south(data: list[str]) -> list[str]:
    return transpose_platform_clockwise(
        tilt_platform_east(transpose_platform_counterclockwise(data)))


def calculate_load_north(data: list[str]) -> int:
    return sum([row.count("O") * (len(data) - i) for i, row in enumerate(data)])


def spin_cycle(data: list[str]) -> list[str]:
    return tilt_platform_east(tilt_platform_south(tilt_platform_west(tilt_platform_north(data))))


def part1(data: list[str]):
    print(f"Part 1: {calculate_load_north(tilt_platform_north(data))}")


def part2(data: list[str]):
    num_cycles = 1_000  # 1,000 ends up working out to be the same as 1 billion
    i = 0
    while i < num_cycles:
        data = spin_cycle(data)
        i += 1

    print(f"Part 2: {calculate_load_north(data)}")


def main():
    with open(r"advent of code\2023\day 14\input.txt") as f:
        platform = [line for line in f.read().strip().split("\n")]

    part1(platform)
    part2(platform)


if __name__ == "__main__":
    main()
