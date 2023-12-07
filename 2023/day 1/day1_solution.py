import re

INPUT_FILE = r"advent of code\2023\day 1\input.txt"


def process_input_data(input_file):
    data = open(input_file, "r").read().split("\n")
    return data


def get_calibration(data):
    calibration_values = []
    for line in data:
        digits = re.findall("(\d)", line)
        value = int(digits[0] + digits[-1]) 
        calibration_values.append(value)

    calibration = sum(calibration_values)
    return calibration


def part1():
    data = process_input_data(INPUT_FILE)
    sum = get_calibration(data)

    print(f"Part 1: {sum}")


def part2():
    data = process_input_data(INPUT_FILE)
    data2 = []
    for line in data:
        line = line.replace("one", "o1e")
        line = line.replace("two", "t2o")
        line = line.replace("three", "t3e")
        line = line.replace("four", "f4r")
        line = line.replace("five", "f5e")
        line = line.replace("six", "s6x")
        line = line.replace("seven", "s7n")
        line = line.replace("eight", "e8t")
        line = line.replace("nine", "n9e")
        
        data2.append(line)
    
    sum2 = get_calibration(data2)
    print(f"Part 2: {sum2}")


if __name__ == "__main__":
    part1()
    part2()
