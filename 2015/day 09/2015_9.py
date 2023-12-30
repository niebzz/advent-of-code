import re
import itertools
from aoc_utils.web import get_puzzle_input


def get_route_info(data: list[str]):
    return [tuple(re.split(" to | = ", line)) for line in data]


def get_possible_routes(route_info: list[tuple]):
    cities = list(set(itertools.chain.from_iterable(
        [route[:2] for route in route_info])))
    return tuple(itertools.permutations(cities))


def measure_distance(city1: str, city2: str, route_info: list[tuple]):
    for route in route_info:
        if city1 in route and city2 in route:
            return int(route[2])


def main():
    data = get_puzzle_input(year=2015, day=9).read().strip().split("\n")
    route_info = get_route_info(data)
    all_routes = get_possible_routes(route_info)

    i = 0
    min_distance = 9999
    max_distance = 0
    while i < len(all_routes):
        distance = 0
        current_route = all_routes[i]
        for j in range(1, len(current_route)):
            distance += measure_distance(current_route[j - 1],
                                         current_route[j],
                                         route_info)
        if distance < min_distance:
            min_distance = distance
        elif distance > max_distance:
            max_distance = distance
        i += 1

    print(f"Part 1: {min_distance}")
    print(f"Part 2: {max_distance}")


if __name__ == "__main__":
    main()
