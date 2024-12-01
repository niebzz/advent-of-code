import re

FILEPATH = r"advent_of_code\2024\day01\input.txt"

with open(FILEPATH) as file:
    input = file.read().split("\n")

# PART 1
list1 = [int(y[0]) for y in [re.findall(r"\d+", x) for x in input]]
list2 = [int(y[1]) for y in [re.findall(r"\d+", x) for x in input]]

total_distance = 0
for location1, location2 in zip(sorted(list1), sorted(list2)):
    total_distance += abs(location2 - location1)

print(f"Part 1: {total_distance}")


# PART 2
def similarity_score(left_ID: int, right_list: list[int]) -> int:
    num_occurences = right_list.count(left_ID)
    return left_ID * num_occurences


total_similarity_score = 0
for ID in list1:
    total_similarity_score += similarity_score(ID, list2)

print(f"Part 2: {total_similarity_score}")
