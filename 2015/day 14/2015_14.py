from re import findall
from aoc_utils.web import get_puzzle_input


def get_distance(reindeer: str, time_sec: int) -> int:
    velocity, travel_time, rest_time = stats[reindeer]
    cycle_time = travel_time + rest_time
    i, distance = 0, 0
    while i < time_sec:
        if (i % cycle_time) in range(travel_time):
            distance += velocity
        i += 1
    return distance


# PART 1
data = get_puzzle_input(year=2015, day=14).read().strip().split("\n")

names = tuple(line.split(" ")[0] for line in data)
digits = tuple([int(x) for x in findall("(\d+)", line)] for line in data)
stats = {k: tuple(v) for k, v in zip(names, digits)}

n = 2503
print(f"Part 1: {max([get_distance(reindeer, n) for reindeer in stats])}")

# PART 2
points = {reindeer: 0 for reindeer in names}
i = 1
while i <= n:
    distances = {reindeer: get_distance(reindeer, i) for reindeer in names}
    lead_pos = max(distances.values())
    for reindeer in names:
        if distances[reindeer] == lead_pos:
            points[reindeer] += 1
    i += 1
print(f"Part 2: {max(points.values())}")
