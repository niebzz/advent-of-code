def increment_character(string: str) -> str:
    return "a" if string == "z" else chr(ord(string) + 1)


def increment_password(string: str) -> str:
    reversed_password = list(string)[::-1]
    z_count = 0
    for i, char in enumerate(reversed_password):
        if char != "z":
            z_count = i
            break
    for i in range(z_count + 1):
        reversed_password[i] = increment_character(reversed_password[i])
    return "".join(reversed_password[::-1])


def three_straight_increasing(string: str) -> bool:
    password = list(string)
    i = 0
    while i < len(password) - 2:
        first = ord(password.pop(0))
        second = ord(password[0])
        third = ord(password[1])
        if (third - second) == 1 and (second - first) == 1:
            return True
    return False


def contains_iol(string: str) -> bool:
    return any(char in "iol" for char in string)


def two_nonoverlapping_pairs(string: str) -> bool:
    password = list(string)
    i = 0
    count = 0
    while i < len(password) - 1:
        first = password.pop(0)
        second = password[0]
        if first == second:
            count += 1
            del password[0]
        if count >= 2:
            return True
    return False


def eight_lowercase(string: str) -> bool:
    if len(string) != 8:
        return False
    if not string.islower():
        return False
    return True


def is_valid_password(string: str) -> bool:
    return eight_lowercase(string) \
        and three_straight_increasing(string) \
        and not contains_iol(string) \
        and two_nonoverlapping_pairs(string)


def part1(string: str):
    input = string
    while True:
        input = increment_password(input)
        if is_valid_password(input):
            break
    return input


def main():
    p1 = part1("hxbxwxba")
    print(f"Part 1: {p1}")

    p2 = part1(p1)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
