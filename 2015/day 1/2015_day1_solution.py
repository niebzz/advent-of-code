with open(r"advent of code\2015\day 1\input.txt") as file:
    data = file.read()

go_up = data.count("(")
go_down = data.count(")")

print(f"Part 1: {go_up - go_down}")

floor = 0
position = 0

for i, char in enumerate(data):
    if char == "(":
        floor = floor + 1
    elif char == ")":
        floor = floor - 1

    if floor == -1:
        position = i + 1
        break
    
print(f"Part 2: {position}")