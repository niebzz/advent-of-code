import time

def get_arrays(input_data):
    instructions = list(input_data[0])
    start_array = [line[0:3] for i, line in enumerate(input_data) if i > 1]
    next_l_array = [line.split("(")[1][0:3] for i, line in enumerate(input_data) if i > 1]
    next_r_array = [line.split(")")[0][-3:] for i, line in enumerate(input_data) if i > 1]
    return instructions, start_array, next_l_array, next_r_array

def steps_required(start_point:str, input_data, part2=False):
    t0 = time.time()
    
    instructions, start_array, next_l_array, next_r_array = get_arrays(input_data)

    instruction_counter = 0
    loop_counter = 0
    pos_counter = 0
    pos_index = start_array.index(start_point)
    position = {}
    position[pos_counter] = start_array[pos_index]

    if not part2:   
        while "ZZZ" != list(position.values())[-1]:
            instruction = instructions[instruction_counter]
            
            if instruction == "L":
                next_l = next_l_array[pos_index]
                next_pos = next_l
                next_r = False # for debugging
            elif instruction == "R":
                next_r = next_r_array[pos_index]
                next_pos = next_r
                next_l = False # for debugging
            else:
                print("Error!")
                exit()

            position[pos_counter + 1] = next_pos

            pos_index = start_array.index(next_pos)
            pos_counter += 1
            loop_counter += 1
            instruction_counter += 1
            
            if instruction_counter >= len(instructions):
                instruction_counter = 0

            if loop_counter % 50000 == 0:
                t1 = time.time()
                print(f"Time Elapsed: {round(t1 - t0,1)} seconds")

        return pos_counter
    
    elif part2:
        exit()
    
def part1():
    INPUT_FILE = r"advent of code\2023\day 8\input.txt"
    data = open(INPUT_FILE).read().split("\n")

    n = steps_required("AAA", data)
    print(f"Part 1: {n}")

part1()



    

    