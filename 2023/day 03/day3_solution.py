import re

input = open(r"advent of code\2023\day 03\input.txt", "r").read()
input = input.split("\n")

num_rows = len(input)
row_length = len(input[0])


def part1():
    valid_part_numbers = []

    symbols = ["`",
               "~",
               "!",
               "@",
               "#",
               "$",
               "%",
               "^",
               "&",
               "*",
               "-",
               "=",
               "+",
               "/",
               "|",
               ":",
               ";",
               "_"
               ]

    for y, line in enumerate(input):
        digits = re.findall("(\d+)", line)
        for digit in digits:
            n = len(digit)
            for match in re.finditer(digit, line):
                start_x = match.start()
                end_x = match.end()
            range_x = n + 2
            range_y = 3
            adjacent_chars = []
            for i in range(range_x):
                x = start_x - 1 + i
                if x < 0:
                    pass
                elif x >= row_length:
                    pass
                else:
                    for j in range(range_y):
                        col = y - 1 + j
                        if col < 0:
                            pass
                        elif col >= num_rows:
                            pass
                        else:
                            adjacent_chars.append(input[col][x])
            for symbol in symbols:
                if symbol in adjacent_chars:
                    valid_part_numbers.append(digit)

    sum = 0
    for part_number in valid_part_numbers:
        value = int(part_number)
        sum = sum + value

    print(f"Part 1 Answer: {sum}")
    return valid_part_numbers, symbols


valid_part_numbers, symbols = part1()


def part2():
    special_characters = {}
    for r in range(len(input)):
        for c, ch in enumerate(input[r]):
            if ch in symbols:
                special_characters[(r, c)] = []

    for r, row in enumerate(input):
        digits = re.finditer("\d+", row)
        for digit in digits:
            for r2 in (r-1, r, r+1):
                for c in range(digit.start()-1, digit.end()+1):
                    if (r2, c) in special_characters:
                        special_characters[(r2, c)].append(int(digit.group()))

    gear_ratios = []
    for values in special_characters.values():
        if len(values) == 2:
            gear_ratio = values[0] * values[1]
            gear_ratios.append(gear_ratio)

    print(f"Part 2 Answer: {sum(gear_ratios)}")


part2()
