from collections import deque


def process_input_data(input_file):
    data = open(input_file).read().splitlines()
    start_row = [i for i, row in enumerate(data) if "S" in row][0]
    start_col = [i for i, char in enumerate(data[start_row]) if char == "S"][0]
    start = (start_row, start_col)

    return data, start


def get_garden_plots(data, start, num_steps):
    start_row, start_col = start[0], start[1]
    results = set()
    seen = {(start_row, start_col)}
    queue = deque([(start_row, start_col, num_steps)])

    while queue:
        row, col, steps = queue.popleft()
        if steps % 2 == 0:
            results.add((row, col))
        if steps == 0:
            continue

        for next_row, next_col in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
            if next_row < 0 or next_col < 0 or next_row >= len(data) or next_col >= len(data[0]):
                continue
            elif data[next_row][next_col] == "#":
                continue
            elif (next_row, next_col) in seen:
                continue
            seen.add((next_row, next_col))
            queue.append((next_row, next_col, steps - 1))

    return results


def part1():
    INPUT_FILE = r"advent of code\2023\day 21\input.txt"

    data, start = process_input_data(INPUT_FILE)
    num_steps = 6 if "test" in INPUT_FILE else 64
    results = get_garden_plots(data, start, num_steps)

    print(f"Part 1: {len(results)}")


part1()
