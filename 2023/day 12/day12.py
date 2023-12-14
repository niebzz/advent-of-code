import itertools

with open(r"advent of code\2023\day 12\input.txt") as f:
    data = [line for line in f.read().strip().split("\n")]


def read_line(line: list):
    springs = line.split(" ")[0]
    clues = [int(x) for x in line.split(" ")[1].split(",")]
    return springs, clues


def get_permutations(string: str) -> list:
    string = tuple(string)
    arr = [".", "#"]
    question_marks = [i for i, x in enumerate(string) if x == "?"]
    q_product = list(itertools.product(arr, repeat=len(question_marks)))
    permutations = []
    for combination in zip(q_product):
        assert len(combination[0]) == len(question_marks)
        new_string = list(string)
        for j, char in enumerate(combination[0]):
            question_mark_index = question_marks[j]
            new_string[question_mark_index] = char
        permutations.append(new_string)
    return permutations


def convert_clues(clues: list) -> list:
    return ["." + ("#"*clue) + "." for clue in clues]


def is_valid_arrangement(line: list, clue_chars: list):
    num_clues = len(tuple(clue_chars))
    i = 0
    j = 0
    # k = 0
    count = 0
    while i <= len(line):
        if j >= len(clue_chars):
            if "#" in "".join(line):
                return False
            else:
                break
        elif clue_chars[j] in "".join(line[:i]):
            count += 1
            del line[:i-1]
            i = 0
            j += 1
        elif "#." in "".join(line[:i]):
            return False
        else:
            i += 1
    return True if count == num_clues else False


total = 0
for i, line in enumerate(data):
    springs, clues = read_line(line)
    print(i, line, clues)
    springs = "." + springs + "."  # prepend and append line with "."
    clues = convert_clues(clues)
    valid_permutations = get_permutations(springs)
    p_count = 0
    for j, permutation in enumerate(valid_permutations):
        is_valid = is_valid_arrangement(permutation, clues)
        if is_valid:
            p_count += 1
    total += p_count

print(f"Part 1: {total}")
