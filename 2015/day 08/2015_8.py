INPUT_FILE = r"advent_of_code\2015\day 8\input.txt"

string_literals = 0
string_values = 0
new_string_values = 0
for string in open(INPUT_FILE):
    string_literals += len(string[:-1])
    string_values += len(eval(string))
    new_string_values += (2 + string.count('\\') + string.count('"'))


print(f"Part 1: {string_literals - string_values + 1}")
print(f"Part 2: {new_string_values}")
