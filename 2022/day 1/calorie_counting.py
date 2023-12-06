
input_path = r"C:\Users\jaken\anaconda3\my_sandbox\advent of code\2022\day 1\input.txt"
input = open(input_path).read().split("\n")

num_elves = int(len([x for x in input if x == ""])) + 1

elf = 1
calories = 0
array = []

for i, item in enumerate(input):
    
    if i == len(input) - 1:
        calories = int(item)
        array.append((elf, calories))

    if item != "":
        calories = calories + int(item)
         
    elif item == "":
        array.append((elf, calories))
        elf = elf + 1
        calories = 0
    

calories = []
for item in array:
    calories.append(item[1])

print(f"Part 1: {max(calories)}")

for i, item in enumerate(calories):
    calories[i] = int(calories[i])

print(f"Part 2: {sum(sorted(calories)[-3:])}")
