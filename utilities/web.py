import os
import requests
import sys
from my_secrets import session_cookie


def get_puzzle_input(year: int, day: int):
    def get_invalid_requests(year: int, day: int):
        if type(year) != int or type(day) != int:
            return TypeError("TypeError: please enter a valid year and date.")
        if year < 2015 or year > 2023:
            return LookupError(f"LookupError: year {year} does not exist.")
        if day <= 0 or day > 25:
            return LookupError(f"LookupErrror: day {day} does not exist.")

    error_msg = get_invalid_requests(year, day)
    if error_msg is not None:
        return print(error_msg)

    # sys.path[0] is always the directory containing the script used to invoke the Python interpreter.
    current_directory = sys.path[0] + "\\"
    file_name = "input.txt"
    input_file = current_directory + file_name

    if os.path.isfile(input_file):
        return open(input_file, "r").read()

    puzzle_input = requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input", cookies=session_cookie).text.strip()

    with open(input_file, "w") as f:
        f.write(puzzle_input)
        print(f"Input file for {year} day {day} created.")

    return open(input_file, "r").read()
