from itertools import permutations
from aoc_utils.web import get_puzzle_input


def get_happiness_info(data: list) -> dict:
    happiness_info = {}
    for line in data:
        name1 = line.split(" ")[0]
        name2 = line.split(" ")[-1][:-1]
        score = int(line.split(" ")[3]) * int(-1 if "lose" in line else 1)
        happiness_info[(name1, name2)] = score
    return happiness_info


def get_names(data: list):
    name1 = set(line.split(" ")[0] for line in data)
    name2 = set(line.split(" ")[-1][:-1] for line in data)
    return tuple(name1 & name2)


def get_permutations(names: tuple):
    return tuple(permutations(names))


def total_happiness(seating_arrangement: tuple, happiness_info: dict):
    total = 0
    # print(seating_arrangement)
    for i, name in enumerate(seating_arrangement):
        left_name = seating_arrangement[i - 1]
        if i == len(seating_arrangement) - 1:
            right_name = seating_arrangement[0]
        else:
            right_name = seating_arrangement[i + 1]
        left_score = happiness_info[(name, left_name)]
        right_score = happiness_info[(name, right_name)]
        total += left_score + right_score
        # print(name, (left_name, right_name), score)
    return total


def part1():
    data = get_puzzle_input(year=2015, day=13).read().split("\n")

#     data = """Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.""".split("\n")

    happiness_info = get_happiness_info(data)
    names = get_names(data)

    max_score = 0
    for i, seating_arrangement in enumerate(get_permutations(names)):
        score = total_happiness(seating_arrangement, happiness_info)
        if score > max_score:
            max_score = score

    print(f"Part 1: {max_score}")
    return happiness_info


part1()
