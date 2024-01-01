import re
from random import shuffle
from aoc_utils.web import get_puzzle_input


with get_puzzle_input(year=2015, day=19) as f:
    replacements, molecule = f.read().split("\n\n")


replacements_list = [tuple(line.split(" => "))
                     for line in replacements.split("\n")]
chars_to_replace = tuple(x[0] for x in replacements_list)
replacement_chars = tuple(x[1] for x in replacements_list)


def part1():
    new_molecules = []
    for (char, new_char) in zip(chars_to_replace, replacement_chars):
        for match_obj in re.finditer(char, molecule):
            new = list(molecule)
            i = match_obj.start()
            new[i] = new_char
            if len(char) == 2:
                del new[i+1]
            new_molecules.append("".join(new))

    distinct_molecules = set(new_molecules)
    print(f"Part 1: {len(distinct_molecules)}")


def part2():
    target = molecule
    count = 0
    while target != 'e':
        tmp = target
        for left, right in replacements_list:
            if right not in target:
                continue

            target = target.replace(right, left, 1)
            count += 1

        if tmp == target:
            target = molecule
            count = 0
            shuffle(replacements_list)
    print(f"Part 2: {count}")


if __name__ == "__main__":
    part1()
    part2()
