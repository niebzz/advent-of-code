from itertools import product
import time
from aoc_utils.web import get_puzzle_input


properties = {
    "Sprinkles": {"capacity": 5, "durability": -1, "flavor": 0, "texture": 0, "calories": 5},
    "PeanutButter": {"capacity": -1, "durability": 3, "flavor": 0, "texture": 0, "calories": 1},
    "Frosting": {"capacity": 0, "durability": -1, "flavor": 4, "texture": 0, "calories": 6},
    "Sugar": {"capacity": -1, "durability": 0, "flavor": 0, "texture": 2, "calories": 8}
}


def calculate_score(combination):
    total_score = 1
    for prop in ["capacity", "durability", "flavor", "texture"]:
        prop_score = sum(properties[ingredient][prop] *
                         amount for ingredient, amount in combination.items())
        total_score *= max(prop_score, 0)
    return total_score


def calculate_calories(combination):
    return sum(properties[ingredient]["calories"] * amount for ingredient, amount in combination.items())


def get_max_score(calories=False):
    score, max_score = 0, 0
    best_combination = None
    for combo in product(range(101), repeat=4):
        if sum(combo) == 100:
            combination = dict(zip(properties.keys(), combo))
            if calories:
                score = calculate_score(combination) if calculate_calories(
                    combination) == 500 else 0
            else:
                score = calculate_score(combination)

            if score > max_score:
                max_score = score

    return max_score


t1 = time.time()
print(f"Part 1: {get_max_score()}; {time.time() - t1} sec")
t2 = time.time()
print(f"Part 2: {get_max_score(calories=True)}; {time.time() - t2} sec")
