import re
import time
from aoc_utils.web import get_puzzle_input


def read_line(line: str):
    r1, c1, r2, c2 = re.findall("(\d+)", line)
    coordinate_pair1 = (int(r1), int(c1))
    coordinate_pair2 = (int(r2), int(c2))
    instruction = line[:(line.find(r1, 0)) - 1]

    return instruction, coordinate_pair1, coordinate_pair2


def toggle_lights(instruction: str, coordinate_pair1: (tuple), coordinate_pair2: (tuple)):
    r1, c1 = coordinate_pair1[0], coordinate_pair1[1]
    r2, c2 = coordinate_pair2[0], coordinate_pair2[1]

    match instruction:
        case "turn on":
            for row in range(min(r1, r2), max(r1, r2) + 1):
                for col in range(min(c1, c2), max(c1, c2) + 1):
                    grid[row][col] = on
            return grid

        case "turn off":
            for row in range(min(r1, r2), max(r1, r2) + 1):
                for col in range(min(c1, c2), max(c1, c2) + 1):
                    grid[row][col] = off
            return grid

        case "toggle":
            for row in range(min(r1, r2), max(r1, r2) + 1):
                for col in range(min(c1, c2), max(c1, c2) + 1):
                    if grid[row][col] == off:
                        grid[row][col] = on
                    elif grid[row][col] == on:
                        grid[row][col] = off
            return grid

    return LookupError("Invalid instructions.")


def count_lights(grid):
    count = 0
    for i, row in enumerate(grid):
        for j in range(len(row)):
            if grid[i][j] == on:
                count += 1
    return count


def set_brightness(instruction: str, coordinate_pair1: (tuple), coordinate_pair2: (tuple)):
    r1, c1 = coordinate_pair1[0], coordinate_pair1[1]
    r2, c2 = coordinate_pair2[0], coordinate_pair2[1]

    match instruction:
        case "turn on":
            for row in range(min(r1, r2), max(r1, r2) + 1):
                for col in range(min(c1, c2), max(c1, c2) + 1):
                    brightness_grid[row][col] = str(
                        int(brightness_grid[row][col]) + 1)
            return brightness_grid

        case "turn off":
            for row in range(min(r1, r2), max(r1, r2) + 1):
                for col in range(min(c1, c2), max(c1, c2) + 1):
                    brightness_grid[row][col] = str(
                        max(0, int(brightness_grid[row][col]) - 1))
            return brightness_grid

        case "toggle":
            for row in range(min(r1, r2), max(r1, r2) + 1):
                for col in range(min(c1, c2), max(c1, c2) + 1):
                    brightness_grid[row][col] = str(
                        int(brightness_grid[row][col]) + 2)
            return brightness_grid

    return LookupError("Invalid instructions.")


def measure_brightness(brightness_grid):
    brightness = 0
    for i, row in enumerate(grid):
        for j in range(len(row)):
            brightness += int(brightness_grid[i][j])
    return brightness


def part1():
    start = time.time()

    for line in data:
        instruction, coordinate1, coordinate2 = read_line(line)
        grid = toggle_lights(instruction, coordinate1, coordinate2)

    end = time.time()
    print(f"Part 1: {count_lights(grid)}, time: {end - start} sec")


def part2():
    start = time.time()

    for line in data:
        instruction, coordinate1, coordinate2 = read_line(line)
        brightness_grid = set_brightness(instruction, coordinate1, coordinate2)

    end = time.time()
    print(
        f"Part 2: {measure_brightness(brightness_grid)}, time: {end - start} sec")


# MAIN
if __name__ == "__main__":
    data = get_puzzle_input(year=2015, day=6).read().split("\n")
    on = "★"
    off = "."
    n = 1000
    grid = [list(off * n) for _ in range(n)]
    brightness_grid = [list("0" * n) for _ in range(n)]

    part1()
    part2()
