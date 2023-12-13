import re

input = open(r"advent of code\2023\day 04\input.txt", "r").read()
input = input.split("\n")

num_rows = len(input)
row_length = len(input[0])


def get_winning_cards(line: str):  # operates in a single line or element in a list
    x = line.split(":")

    winning_cards = x[1].split("|")[0]
    winning_cards = re.findall("(\d+)", winning_cards)

    my_cards = x[1].split("|")[1]
    my_cards = re.findall("(\d+)", my_cards)

    my_winning_cards = [int(card)
                        for card in my_cards if card in winning_cards]
    num_winning_cards = len(my_winning_cards)

    return (my_winning_cards, num_winning_cards)


def calculate_points(num_winning_cards: int):
    points = 0
    if num_winning_cards == 0:
        pass
    else:
        # formula for point calculation = 2^(n-1)
        points = 2**(num_winning_cards-1)

    return points


def part1(input_file):
    sum = 0
    for line in input_file:
        (my_winning_cards, num_winning_cards) = get_winning_cards(line)  # tuple
        points = calculate_points(num_winning_cards)
        sum = sum + points
    return sum


print(f"Part 1: {part1(input)}")


matches = [len(set(line[:40].split()) & set(line[42:].split()))
           for line in input]

cards = [1] * len(matches)

for i, n in enumerate(matches):
    for j in range(n):
        cards[i + j + 1] += cards[i]

print(f"Part 2: {sum(cards)}")
