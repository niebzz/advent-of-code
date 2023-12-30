import os
import requests
import sys
from aoc_utils.my_secrets import session_cookie


def get_puzzle_input(year: int, day: int):
    def get_invalid_requests(year: int, day: int):
        if type(year) != int or type(day) != int:
            raise TypeError("Please enter a valid year and date.")
        if year < 2015 or year > 2023:
            raise LookupError(f"Year {year} does not exist.")
        if day <= 0 or day > 25:
            raise LookupError(f"Day {day} does not exist.")

    get_invalid_requests(year, day)

    # sys.path[0] is always the directory containing the script used to invoke the Python interpreter.
    current_directory = sys.path[0] + "\\"
    file_name = "input.txt"
    input_file = current_directory + file_name

    if os.path.isfile(input_file):
        return open(input_file, "r")

    puzzle_input = requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies=session_cookie,
        timeout=10).text.strip()

    with open(input_file, "w") as f:
        f.write(puzzle_input)
        print(f"Input file for {year} day {day} created.")

    return open(input_file, "r")
