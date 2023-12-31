import re
from aoc_utils.web import get_puzzle_input


input = get_puzzle_input(year=2015, day=16).read().strip().split("\n")
ticker_tape = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""


def get_input_dict(input: list[str]) -> dict:
    input_dict = {}
    for line in input:
        info = [x for x in re.split("[:, ]", line) if x != ""]
        sue = info[0] + " " + info[1]
        labels = info[2:][0::2]
        numbers = [int(x) for i, x in enumerate(info[2:]) if x not in labels]
        input_dict[sue] = {k: int(v) for k, v in zip(labels, numbers)}

    return input_dict


def is_valid_p1(key: str) -> bool:
    for item in sue_dict[key]:
        if sue_dict[key][item] != ticker_tape[item]:
            return False
    return True


def is_valid_p2(key: str) -> bool:
    for item in sue_dict[key]:
        if item in ["cats", "trees"]:
            if sue_dict[key][item] <= ticker_tape[item]:
                return False
        elif item in ["pomeranians", "goldfish"]:
            if sue_dict[key][item] >= ticker_tape[item]:
                return False
        else:
            if sue_dict[key][item] != ticker_tape[item]:
                return False
    return True


if __name__ == "__main__":
    sue_dict = get_input_dict(input)
    ticker_tape = {k: int(v) for k, v in [line.split(
        ": ") for line in ticker_tape.split("\n")]}

    p1 = [sue for sue in sue_dict if is_valid_p1(sue)][0]
    p2 = [sue for sue in sue_dict if is_valid_p2(sue)][0]

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
