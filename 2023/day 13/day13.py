
def intersect_multiple_lists(list_of_lists: list[list]) -> list:
    return list(set.intersection(*map(set, list_of_lists)))

    
def find_reflections(row: str) -> list:
    ls = list(row)

    valid_reflections = []
    for r in range(1, len(ls)):
        left = ls[r:]
        right = ls[:r][::-1]
        left = left[:len(right)]
        right = right[:len(left)]
        if left == right:
            valid_reflections.append(r)

    return valid_reflections


def find_mirror(grid: list) -> int:
    possible_mirrors = []
    for row in grid:
        reflections = find_reflections(row)
        possible_mirrors.append(reflections)
    mirror = intersect_multiple_lists(possible_mirrors)

    assert 0 <= len(mirror) <= 1
    return mirror[0] if len(mirror) == 1 else 0


def part1():
    grids = []
    total = 0
    for block in open(r"advent of code\2023\day 13\input.txt").read().split("\n\n"):
        grid = block.splitlines()
        grids.append(grid)
        vert_mirrors = find_mirror(grid)
        horiz_mirrors = find_mirror(list(zip(*grid)))
        total += (horiz_mirrors * 100) + vert_mirrors
    print(f"Part1: {total}")
    return grids

part1()