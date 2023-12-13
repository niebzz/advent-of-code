import matplotlib.pyplot as plt


def map_grid(input_data: list) -> dict:
    grid = {}
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            grid[(i, j)] = input_data[i][j]
    return grid


def find_S(grid: dict) -> tuple:
    return [key for key in grid if grid[key] == "S"][0]


def get_pipe(position: tuple, grid: dict) -> str:
    return grid[position]


def get_next_position(position: tuple, direction: str, grid: dict) -> tuple:
    north = 0
    south = 0
    east = 0
    west = 0
    match direction:
        case "north":
            north = 1
        case "south":
            south = 1
        case "east":
            east = 1
        case "west":
            west = 1

    next_row = position[0] + south - north
    next_col = position[1] + east - west
    next_pos = (next_row, next_col)

    new_dir = direction
    next_pipe = get_pipe(next_pos, grid)
    match next_pipe:
        case "|":
            if direction == "east" or direction == "west":
                return None
        case "-":
            if direction == "north" or direction == "south":
                return None
        case "L":
            if direction == "south":
                new_dir = "east"
            elif direction == "west":
                new_dir = "north"
            else:
                return None
        case "J":
            if direction == "south":
                new_dir = "west"
            elif direction == "east":
                new_dir = "north"
            else:
                return None
        case "7":
            if direction == "east":
                new_dir = "south"
            elif direction == "north":
                new_dir = "west"
            else:
                return None
        case "F":
            if direction == "north":
                new_dir = "east"
            elif direction == "west":
                new_dir = "south"
            else:
                return None
        case ".":
            return None
        case "S":
            pass
    return next_pos, new_dir


def part1():
    with open(r"advent of code\2023\day 10\input.txt") as file:
        input_data = file.read().strip().split("\n")

    grid = map_grid(input_data)
    s = find_S(grid)
    dir = "east"

    new_pos, new_dir = get_next_position(s, dir, grid)
    new_pipe = get_pipe(new_pos, grid)
    step_count = 1
    main_loop = {new_pos: step_count}
    while new_pipe != "S":
        new_pos, new_dir = get_next_position(new_pos, new_dir, grid)
        new_pipe = get_pipe(new_pos, grid)
        step_count += 1
        main_loop[new_pos] = step_count

    furthest_point = int(step_count / 2)
    print(f" Part 1: {furthest_point}")

    return s, input_data, grid, main_loop, step_count


s, input_data, grid, main_loop, step_count = part1()


def part2():
    grid[s] = "L"  # manually replacing S character

    data = [["."]*len(line) for line in input_data]
    for (r, c) in grid:
        if (r, c) in main_loop:
            data[r][c] = grid[(r, c)]

    total_count = 0
    inside = {}
    for r, row in enumerate(data):
        line_count = 0
        odd_number = False
        for c, ch in enumerate(row):
            if ch == "|":
                odd_number = not odd_number
            elif ch == "F":
                odd_number = not odd_number
            elif ch == "7":
                odd_number = not odd_number
            elif ch == ".":
                if odd_number:
                    line_count += 1
                    inside[(r, c)] = "I"

        total_count += line_count
    print(f"Part2: {total_count}")

    return total_count, inside


total_count, inside = part2()

# extra plotting
rows = [pos[0] for pos in main_loop]
cols = [pos[1] for pos in main_loop]
inside_rows = [pos[0] for pos in inside]
inside_cols = [pos[1] for pos in inside]

plt.plot(rows, cols, "b", label="Main Loop")
plt.plot(s[1], s[0], "ro", label="S")
plt.plot(inside_rows, inside_cols, "g*", label="Enclosed Tiles")
plt.gca().invert_yaxis()
plt.show()
