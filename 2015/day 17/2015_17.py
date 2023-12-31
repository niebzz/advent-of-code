from itertools import combinations
from math import factorial
from aoc_utils.web import get_puzzle_input


def count_combinations(containers, target_volume):
    count = 0
    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target_volume:
                count += 1
    return count


def min_containers_for_volume(containers, target_volume):
    containers.sort(reverse=True)

    min_containers = len(containers)
    best_combinations = []

    for r in range(1, len(containers) + 1):
        for combo in combinations(containers, r):
            if sum(combo) == target_volume:
                if r < min_containers:
                    min_containers = r
                    best_combinations = [combo]
                elif r == min_containers:
                    best_combinations.append(combo)

    return best_combinations


def part1():
    return count_combinations(containers, target_volume)


def part2():
    return len(min_containers_for_volume(containers, target_volume))


containers = [int(x) for x in get_puzzle_input(
    year=2015, day=17).read().split("\n")]
target_volume = 150


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
