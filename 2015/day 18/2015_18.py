from aoc_utils.web import get_puzzle_input


def display_grid(grid: list[list]):
    print("-----GRID-----")
    for row in grid:
        print(row)


def get_adjacent_coordinates(row: int, col: int, grid: list[list]):
    dr = set([max(0, row - 1), row, min(row + 1, len(grid) - 1)])
    dc = set([max(0, col - 1), col, min(col + 1, len(grid[row]) - 1)])

    return [x for x in [(r, c) for r in dr for c in dc] if x != (row, col)]


def get_next_state(row: int, col: int, grid: list[list]):
    char = grid[row][col]
    adj_chars = [grid[r][c]
                 for (r, c) in get_adjacent_coordinates(row, col, grid)]
    num_on = len([x for x in adj_chars if x == "#"])

    if char == "#" and num_on not in [2, 3]:
        char = "."
    elif char == "." and num_on == 3:
        char = "#"

    return char


def flip_lights(grid: list[list]):
    return [[get_next_state(r, c, grid) for c in range(len(row))]
            for r, row in enumerate(grid)]


def count_on_lights(grid: list[list]):
    total = 0
    for i, row in enumerate(grid):
        for j in range(len(row)):
            if grid[i][j] == "#":
                total += 1
    return total


def part1(grid):
    for _ in range(100):
        grid = flip_lights(grid)

    print(f"Part 1: {count_on_lights(grid)}")


def turn_corners_on(grid: list[list]):
    h = len(grid) - 1
    w = len(grid[0]) - 1
    corners = [(0, 0), (0, w), (h, 0), (h, w)]
    for corner in corners:
        grid[corner[0]][corner[1]] = "#"
    return grid


def part2(grid: list[list]):
    for _ in range(100):
        grid = flip_lights(turn_corners_on(grid))

    grid = turn_corners_on(grid)

    print(f"Part 2: {count_on_lights(grid)}")


def main():
    input = get_puzzle_input(year=2015, day=18).read().split("\n")
    grid = [list(row) for row in input]

    part1(grid)
    part2(grid)


if __name__ == "__main__":
    main()
