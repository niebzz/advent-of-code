path = r"C:\Users\jaken\anaconda3\my_sandbox\advent of code\2022\day 2\input.txt"
strategy_guide = open(path).read().split("\n")

# --- Part One ---
opp_dict = {"A": "rock", "B": "paper", "C": "scissors"}
my_dict = {"X": "rock", "Y": "paper", "Z": "scissors"}

result_dict = {"AX": "draw",
               "AY": "win",
               "AZ": "lose",
               "BX": "lose",
               "BY": "draw",
               "BZ": "win",
               "CX": "win",
               "CY": "lose",
               "CZ": "draw"}

win_points_dict = {"win": 6, "draw": 3, "lose": 0}
my_points_dict = {"rock": 1, "paper": 2, "scissors": 3}

all_points = []
for i, line in enumerate(strategy_guide):
    game = line.replace(" ", "")
    my_move = my_dict[game[1]]
    my_points = my_points_dict[my_move]
    result = result_dict[game]
    game_points = win_points_dict[result]
    points = my_points + game_points
    all_points.append(points)


print(f"P1: {sum(all_points)}")

# --- Part Two ---

p2_result_dict = {"AX": "lose",
                  "AY": "draw",
                  "AZ": "win",
                  "BX": "lose",
                  "BY": "draw",
                  "BZ": "win",
                  "CX": "lose",
                  "CY": "draw",
                  "CZ": "win"}


p2_my_dict  =    {"AX": "scissors",
                  "AY": "rock",
                  "AZ": "paper",
                  "BX": "rock",
                  "BY": "paper",
                  "BZ": "scissors",
                  "CX": "paper",
                  "CY": "scissors",
                  "CZ": "rock"}


all_points = []
for i, line in enumerate(strategy_guide):
    game = line.replace(" ", "")
    result = p2_result_dict[game]
    game_points = win_points_dict[result]
    my_points = my_points_dict[p2_my_dict[game]]
    points = game_points + my_points
    all_points.append(points)

print(f"P2: {sum(all_points)}")