INPUT_FILE = r"advent of code\2023\day 18\input.txt"


def dig_hole(trench: list, r: int, c: int, line: str, part2=False):
    direction = line.split(" ")[0]
    cubic_meters = int(line.split(" ")[1])

    if part2:
        true_instruction = line.split("(")[1][1:-1]
        true_direction = int(true_instruction[-1])
        match true_direction:
            case 0:
                direction = "R"
            case 1:
                direction = "D"
            case 2:
                direction = "L"
            case 3:
                direction = "U"

        cubic_meters = int(line.split("(")[1][1:-2], 16)

    match direction:
        case "R":
            dr, dc = 0, cubic_meters
        case "L":
            dr, dc = 0, -1 * cubic_meters
        case "U":
            dr, dc = -1 * cubic_meters, 0
        case "D":
            dr, dc = cubic_meters, 0

    new_r = r + dr
    new_c = c + dc
    trench.append((new_r, new_c))

    return trench, new_r, new_c, cubic_meters


def dig_perimiter(input_data, part2=False):
    r, c = 0, 0
    points = [(r, c)]
    num_points = 0
    for line in input_data:
        points, r, c, cubic_meters = dig_hole(points, r, c, line, part2)
        num_points += cubic_meters

    return points, num_points


def calculate_area(points: list):  # shoelace formula
    two_times_area = 0
    for i in range(len(points)):
        x1 = points[i][0]
        x2 = points[(i + 1) % len(points)][0]
        y1 = points[i][1]
        y2 = points[(i + 1) % len(points)][1]
        two_times_area += (x1 * y2) - (x2 * y1)

    area = abs(two_times_area) // 2

    return area


def get_points(data, part2=False):
    points, boundary_points = dig_perimiter(data, part2)
    area = calculate_area(points)
    interior_points = (area - boundary_points // 2) + 1
    total_points = boundary_points + interior_points

    return total_points


def part1():
    with open(INPUT_FILE) as f:
        data = f.read().strip().split("\n")

    total_points = get_points(data)
    print(f"Part 1: {total_points}")


def part2():
    with open(INPUT_FILE) as f:
        data = f.read().strip().split("\n")

    total_points = get_points(data, part2=True)
    print(f"Part 2 {total_points}")


part1()
part2()
