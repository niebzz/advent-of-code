import hashlib

INPUT = "yzbqklnj"


def part1():
    i = 0
    first5 = 0
    while first5 != "00000":
        str2hash = INPUT + str(i)
        md5 = hashlib.md5(str2hash.encode()).hexdigest()
        first5 = md5[:5]
        i += 1

    print(f"Part 1: {i - 1}")


def part2():
    i = 0
    first6 = 0
    while first6 != "000000":
        str2hash = INPUT + str(i)
        md5 = hashlib.md5(str2hash.encode()).hexdigest()
        first6 = md5[:6]
        i += 1

    print(f"Part 2: {i - 1}")


if __name__ == "__main__":
    part1()
    part2()
