def look_and_say(string: str):
    chars = list(string)
    copies = 0
    new_string = []
    for i in range(len(chars)):
        digit = chars[i]
        if chars[i] == chars[min(i + 1, len(chars) - 1)]:
            copies += 1
        else:
            copies += 1
            new_string.append(copies)
            new_string.append(digit)
            copies = 0
        if i == len(chars) - 1:
            new_string.append(copies)
            new_string.append(digit)

    return "".join([str(x) for x in new_string])


def part1():
    input = "1113222113"
    for _ in range(40):
        input = look_and_say(input)

    print(f"Part 1: {len(input)}")


def part2():
    input = "1113222113"
    for _ in range(50):
        input = look_and_say(input)

    print(f"Part 2: {len(input)}")


if __name__ == "__main__":
    part1()
    part2()
