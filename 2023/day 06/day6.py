import re
import math

input_file = r"advent of code\2023\day 06\input.txt"

data = open(input_file).read().split("\n")
data = [re.findall("(\d+)", line) for line in data]

opp_races = []

for i in range(len(data[0])):
    time, opp_distance = (int(data[0][i]), int(data[1][i]))

    opp_races.append((time, opp_distance))

def get_ways_to_win(races: list) -> list: # races = [(time1, distance1), (time2, distance2), etc.]
    ways_to_win = []

    for i, race in enumerate(races):
        num_ways_to_win = 0

        time = race[0]
        time_range = [t for t in range(0, time + 1)]

        distance_to_beat = race[1]

        for j in range(len(time_range)):
            hold_time = j
            travel_time = time - hold_time

            velocity = hold_time 
            distance = travel_time * velocity
            
            if distance > distance_to_beat:
                num_ways_to_win = num_ways_to_win + 1
                
        ways_to_win.append(num_ways_to_win)

    return ways_to_win


p1 = math.prod(get_ways_to_win(opp_races))

print(f"Part 1: {p1}")

time = []
distance = []
for i in range(len(data[0])):
    time.append(data[0][i])
    distance.append(data[1][i])

time = int("".join(time))
distance = int("".join(distance))

race2 = [(time, distance)]

p2 = get_ways_to_win(race2)[0]
print(f"Part 2: {p2}")