import re

INPUT_FILE = r"advent of code\2023\day 9\input.txt"
data = open(INPUT_FILE).read().split("\n")
digits = [re.findall("[+-]?\d+", line) for line in data]


def get_steps(line: list, part2=False) -> list:
    steps = []
    for i, digit in enumerate(line):
        if i >= len(line) - 1:
            break
        step = int(line[i+1]) - int(digit)
        if part2:
            step = step * -1
        steps.append(step)
    return steps


def get_pyramid(line: list, part2=False) -> list:
    lines = []
    original_line = [int(x) for x in line]
    new_line = line
    lines.append(original_line)
    while not all(num == 0 for num in new_line):
        new_line = get_steps(new_line, part2)
        lines.append(new_line)
    return lines


def get_pyramid_history(pyramid: list, part2=False) -> int:
    pyramid.reverse()
    history_values = [0]
    for i, row in enumerate(pyramid):
        if i >= len(pyramid) - 1:
            break
        if not part2:
            next_history = row[-1] + pyramid[i+1][-1]
        elif part2:
            next_history = pyramid[i+1][-1] - row[-1]

        history_values.append(next_history)
        pyramid[i+1].append(next_history)
    return history_values[-1]


def get_line_history(line: list, part2=False):
    pyramid = get_pyramid(line, part2)
    history = get_pyramid_history(pyramid, part2)
    return history


def reverse_input_data(list_of_lists: list):
    reversed_lists = []
    for list in list_of_lists:
        list.reverse()
        reversed_lists.append(list)
    return reversed_lists


def part1():
    h_sum = 0
    for line in digits:
        lh = get_line_history(line)
        h_sum = h_sum + lh
    print(f"Part 1: {h_sum}")


def part2():
    digits2 = reverse_input_data(digits)
    h_sum = 0
    for line in digits2:
        lh = get_line_history(line, part2=True)
        h_sum = h_sum + lh
    print(f"Part 2: {h_sum}")


part1()
part2()