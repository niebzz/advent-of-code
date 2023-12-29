from utilities.web import get_puzzle_input


def has_three_vowels(line: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    count = len([char for char in line if char in vowels])
    return False if count < 3 else True


def has_two_letters_in_a_row(line: str) -> bool:
    for i, char in enumerate(line):
        if i == len(line) - 1:
            return False
        if line[i + 1] == char:
            return True


def has_no_invalid_strings(line: str) -> bool:
    invalid_strings = ["ab", "cd", "pq", "xy"]
    for string in invalid_strings:
        if string in line:
            return False
    return True


def has_two_letters_in_a_row_that_appear_twice_and_dont_overlap(line: str) -> bool:
    i = 1
    while i < len(line):
        possible_pair = line[i-1] + line[i]
        if possible_pair in line[i+1:]:
            return True
        i += 1
    return False


def contains_one_letter_which_repeats_after_exactly_one_letter_between_them(line: str) -> bool:
    for i, char in enumerate(line):
        if i == len(line) - 2:
            return False
        if line[i + 2] == char:
            return True


def is_nice(line: str, part2=False) -> bool:
    if part2:
        return has_two_letters_in_a_row_that_appear_twice_and_dont_overlap(line) and contains_one_letter_which_repeats_after_exactly_one_letter_between_them(line)
    else:
        return has_three_vowels(line) and has_two_letters_in_a_row(line) and has_no_invalid_strings(line)


if __name__ == "__main__":
    data = get_puzzle_input(
        year=2015, day=5, input_file=r"advent_of_code\2015\day 5\input.txt").strip().split("\n")

    p1 = sum([1 for line in data if is_nice(line)])
    p2 = sum([1 for line in data if is_nice(line, part2=True)])

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
