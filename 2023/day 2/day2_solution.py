import re

input = open("input.txt", "r").readlines()

total_red = 12;
total_green = 13;
total_blue = 14;

invalid_games = []

for row in input:
    game = row.split(":", maxsplit = 1)[0]
    sets = row.replace(game + ': ', '').split(";")

    for set in sets:
        num_red = re.findall(r"(\d+) red", set)
        num_green = re.findall(r"(\d+) green", set)
        num_blue = re.findall(r"(\d+) blue", set)

        # red
        if len(num_red) == 0:
            continue
        else:
            if int(num_red[0]) > total_red:
                invalid_games.append(game)
                # print(f"{game} invalid: more than {total_red} red found in [{set}]")
                break

        # green
        if len(num_green) == 0:
            continue
        else:
            if int(num_green[0]) > total_green:
                invalid_games.append(game)
                # print(f"{game} invalid: more than {total_green} green found in [{set}]")
                break

        # blue
        if len(num_blue) == 0:
            continue
        else:
            if int(num_blue[0]) > total_blue:
                invalid_games.append(game)
                # print(f"{game} invalid: more than {total_blue} blue found in [{set}]")
                break
    

valid_games = []

for row in input:
    game = row.split(":", maxsplit = 1)[0]

    if game in invalid_games:
        continue
        # print(f"{game} is invalid.")
    else:
        # print(f"{game} is valid.")
        valid_games.append(game)

sum = 0
for game in valid_games:
    ID = int(game.split(" ")[1])

    sum = sum + ID

print(f"""
---
    Part 1 Sum: {sum}
---""")
  

# Part 2
fewest_red = []
fewest_green = []
fewest_blue = []


for row in input:
    game = row.split(":", maxsplit = 1)[0]
    sets = row.split(":", maxsplit = 1)[1]

    num_red = re.findall(r"(\d+) red", sets)
    num_red = [eval(item) for item in num_red]

    num_green = re.findall(r"(\d+) green", sets)
    num_green = [eval(item) for item in num_green]

    num_blue = re.findall(r"(\d+) blue", sets)
    num_blue = [eval(item) for item in num_blue]

    fewest_red.append(max(num_red))
    fewest_green.append(max(num_green))
    fewest_blue.append(max(num_blue))



power = []

for i in range(len(fewest_red)):
    power_i = fewest_red[i] * fewest_green[i] * fewest_blue[i]

    power.append(power_i)

sum = 0

for item in power:
    sum = sum + item

print(f"""---
    Part 2 Sum: {sum}
---""")