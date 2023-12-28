import requests
import os
from my_secrets import session_cookie


def get_invalid_requests(year: int, day: int, input_file: str):
    if type(year) != int or type(day) != int:
        return TypeError("TypeError: please enter a valid year and date.")
    if year < 2015 or year > 2023:
        return LookupError(f"LookupError: year {year} not found.")
    if day <= 0 or day > 25:
        return LookupError(f"LookupErrror: day {day} not found.")
    if input_file[-4:] != ".txt":
        return TypeError("Invalid input file (.txt).")


def get_puzzle_input(year: int, day: int, input_file: str) -> None:

    error_msg = get_invalid_requests(year, day, input_file)
    if error_msg is not None:
        return print(error_msg)

    if os.path.isfile(input_file):
        return open(input_file, "r").read()

    puzzle_input = requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input", cookies=session_cookie).text.strip()

    with open(input_file, "w") as f:
        f.write(puzzle_input)
        print(f"Input file for {year} day {day} created.")

    with open(input_file, "r") as f:
        return f.read()
