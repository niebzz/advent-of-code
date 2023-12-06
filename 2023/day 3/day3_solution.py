import re

input = open(r"input.txt", "r").read()
input = input.split("\n")

num_rows = len(input)
row_length = len(input[0])
# print(num_rows)

valid_part_numbers = []

symbols = ["`",
           "~",
           "!",
           "@",
           "#",
           "$",
           "%",
           "^",
           "&",
           "*",
           "-",
           "=",
           "+",
           "/",
           "|",
           ":",
           ";",
           "_"
           ]

for y, line in enumerate(input):
    digits = re.findall("(\d+)", line)

    for digit in digits:
        n = len(digit)
        # print(n)

        for match in re.finditer(digit, line):
            start_x = match.start()
            end_x = match.end()

        range_x = n + 2
        range_y = 3

        print(f"Digit: {digit}; x: {start_x}...{end_x}; y: {y}")

        adjacent_chars = []

        for i in range(range_x):
            x = start_x -1 + i
            
            if x < 0:
                pass
            elif x >= row_length:
                pass
            else:
                
                for j in range(range_y):
                    col = y - 1 + j
                    
                    if col < 0:
                        pass
                    elif col >= num_rows:
                        pass
                    else:
                        print(f"    adjacent cells: (row {x}, col {col}): char = '{input[col][x]}'")
                      
                        
                        adjacent_chars.append(input[col][x])

        # print(f"    adjacent characters = {adjacent_chars}")

        for symbol in symbols:
            if symbol in adjacent_chars:
                valid_part_numbers.append(digit)
                print(f"DIGIT {digit} IS VALID.")
                    
    
    
# print(valid_part_numbers)

sum = 0
for part_number in valid_part_numbers:
    value = int(part_number)
    sum = sum + value

print(f"Part 1 Answer: {sum}")
