def get_coordinate(char: str, row: int, col: int):
    match char:
        case ">":
            return (row, col + 1)
        case "<":
            return (row, col - 1)
        case "^":
            return (row - 1, col)
        case "v":
            return (row + 1, col)

    return KeyError("Invalid character.")


def deliver_presents(data: str):
    r, c = 0, 0
    locations = {(r, c): 1}

    for char in data:
        (r, c) = get_coordinate(char, r, c)

        if (r, c) not in locations:
            locations[(r, c)] = 1
        else:
            locations[(r, c)] += 1
    return locations


def part1(data: str):
    houses = deliver_presents(data)
    print(f"Part 1: {len(houses)}")


def part2(data: str):
    santa_directions = "".join(
        [char for i, char in enumerate(data) if i % 2 == 0])
    robot_directions = "".join(
        [char for i, char in enumerate(data) if i % 2 == 1])

    santa_houses = list(deliver_presents(santa_directions))
    robot_houses = list(deliver_presents(robot_directions))

    all_houses = set(santa_houses + robot_houses)

    print(f"Part 2: {len(all_houses)}")


def main():
    with open(r"advent of code\2015\day 3\input.txt") as f:
        data = f.read()
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
