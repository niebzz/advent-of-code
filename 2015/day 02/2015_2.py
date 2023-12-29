def calculate_surface_area(length: int, width: int, height: int) -> int:
    surface_area = (2 * length * width) + \
        (2 * width * height) + (2 * height * length)
    d1, d2 = sorted([length, width, height])[:2]
    slack_area = d1 * d2
    return surface_area + slack_area


def calculate_volume(length: int, width: int, height: int) -> int:
    return length * width * height


def calculate_ribbon_length(length: int, width: int, height: int) -> int:
    d1, d2 = sorted([length, width, height])[:2]
    shortest_perimeter = (2 * d1) + (2 * d2)
    volume = calculate_volume(length, width, height)
    return volume + shortest_perimeter


def main():
    with open(r"advent of code\2015\day 2\input.txt") as f:
        data = f.read().split("\n")

    wrapping_paper_sqft = 0
    ribbon_length_ft = 0
    for line in data:
        l, w, h = sorted([int(i) for i in line.split("x")])
        wrapping_paper_sqft += calculate_surface_area(l, w, h)
        ribbon_length_ft += calculate_ribbon_length(l, w, h)

    print(f"Part 1: {wrapping_paper_sqft}")
    print(f"Part 2: {ribbon_length_ft}")


if __name__ == "__main__":
    main()
