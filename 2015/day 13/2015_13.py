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
    for i, name in enumerate(seating_arrangement):
        left_name = seating_arrangement[i - 1]
        if i == len(seating_arrangement) - 1:
            right_name = seating_arrangement[0]
        else:
            right_name = seating_arrangement[i + 1]
        left_score = happiness_info[(name, left_name)]
        right_score = happiness_info[(name, right_name)]
        total += left_score + right_score
    return total


def part1(data):
    names = get_names(data)
    happiness_info = get_happiness_info(data)

    max_score = 0
    for i, seating_arrangement in enumerate(get_permutations(names)):
        score = total_happiness(seating_arrangement, happiness_info)
        if score > max_score:
            max_score = score

    return max_score


def part2(data):
    def add_myself():
        names = get_names(data)
        me = "me"
        for name in names:
            data.append(
                f"{me} would gain 0 happiness units by sitting next to {name}.")
            data.append(
                f"{name} would gain 0 happiness units by sitting next to {me}.")
    add_myself()
    return part1(data)


if __name__ == "__main__":
    data = get_puzzle_input(year=2015, day=13).read().split("\n")

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
