def get_empty_rows_cols(data: list[list]):
    rows = [x for x in range(len(data))]
    cols = [x for x in range(len(data[0]))]
    rows_with_galaxies = []
    cols_with_galaxies = []
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char != ".":
                rows_with_galaxies.append(r)
                cols_with_galaxies.append(c)
                pass
    rows_to_expand = list(set(rows) ^ set(rows_with_galaxies))
    cols_to_expand = list(set(cols) ^ set(cols_with_galaxies))
    return rows_to_expand, cols_to_expand


def get_galaxies(data: list[list]):
    galaxies = []
    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if ch == ".":
                pass
            elif ch == "#":
                galaxies.append((r, c))
    return galaxies


def sum_all_galaxy_distances(input_data, multiplier=2):
    empty_rows, empty_cols = get_empty_rows_cols(input_data)
    galaxies = get_galaxies(input_data)

    total = 0
    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += multiplier if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += multiplier if c in empty_cols else 1
    return total


def part1():
    with open(r"advent of code\2023\day 11\input.txt") as f:
        input_data = f.read().strip().split("\n")
        input_data = [list(x) for x in input_data]

    p1_total = sum_all_galaxy_distances(input_data)
    print(f"Part 1: {p1_total}")
    return input_data, p1_total


input_data, p1_total = part1()


def part2():
    p2_total = sum_all_galaxy_distances(input_data, multiplier=1000000)
    print(f"Part 2: {p2_total}")


part2()
