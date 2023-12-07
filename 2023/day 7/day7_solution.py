def process_input_data(input_file: str) -> dict:
    data = open(input_file).read().split("\n")
    dict = {}
    for line in data:
        hand = line.split(" ")[0]
        bid = int(line.split(" ")[1])
        dict[hand] = bid
    return dict


def get_num_occurences(card: str, hand: str):
    x = [i for i, letter in enumerate(hand) if letter == card]
    return len(x)


def five_of_a_kind(string: str) -> bool:
    if len(string) == 5 and len(set(string)) == 1:
        return True
    else:
        return False


def four_of_a_kind(string: str) -> bool:
    card_count = [get_num_occurences(char, string) for char in string]
    if len(string) == 5 and max(card_count) == 4:
        return True
    else:  
        return False


def full_house(string: str) -> bool:
    card_count = [get_num_occurences(char, string) for char in string]
    if list((set(card_count)))[0] == 2 and list((set(card_count)))[1] == 3:
        return True
    else:
        return False


def three_of_a_kind(string: str) -> bool:
    card_count = [get_num_occurences(char, string) for char in string]
    if len(string) == 5 and max(card_count) == 3:
        return True
    else:  
        return False


def two_pair(string: str) -> bool:
    card_count = [get_num_occurences(char, string) for char in string]
    if max(list(set(card_count))) == 2 and card_count.count(2) == 4:
        return True
    else:
        return False


def one_pair(string: str) -> bool:
    card_count = [get_num_occurences(char, string) for char in string]
    if max(list(set(card_count))) == 2 and card_count.count(2) == 2:
        return True
    else:
        return False


def high_card(string: str) -> bool:
    card_count = [get_num_occurences(char, string) for char in string]
    if max(list(set(card_count))) == 1:
        return True
    else:
        return False
    

def evaluate_hand(hand: str):
    # assigns an arbirtary strength value based on the type of hand
    if len(hand) != 5:
        exit()
    elif five_of_a_kind(hand):
        return 7
    elif four_of_a_kind(hand):
        return 6
    elif full_house(hand):
        return 5
    elif three_of_a_kind(hand):
        return 4
    elif two_pair(hand):
        return 3
    elif one_pair(hand):
        return 2
    elif high_card(hand):
        return 1
    else:
        return None
    

def get_relative_strength(char: str):
    ranking = "AKQJT98765432"
    if char not in ranking:
        exit()
    else:
        pos = ranking.find(char)
        relative_strength = len(ranking) - pos
    return relative_strength


def break_ties(tied_hands: list):
    new_ranks = {}
    for hand in tied_hands:
        c1_rs = (get_relative_strength(hand[0]) + 10) ** 40
        c2_rs = (get_relative_strength(hand[1]) + 10) ** 30
        c3_rs = (get_relative_strength(hand[2]) + 10) ** 20
        c4_rs = (get_relative_strength(hand[3]) + 10) ** 10
        c5_rs = (get_relative_strength(hand[4]) + 10) ** 1

        hand_strength = c1_rs + c2_rs + c3_rs + c4_rs + c5_rs
        new_ranks[hand] = hand_strength

    new_ranks = list(dict(sorted(new_ranks.items(), key=lambda item: item[1])).keys())
    return new_ranks


def sort_hands(input_data: dict):
    strength_dict = {}
    for i, hand in enumerate(list(input_data.keys())):
        strength = evaluate_hand(hand)
        strength_dict[hand] = strength
    
    fivekinds   = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 7])
    fourkinds   = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 6])
    fullhouses  = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 5])
    threekinds  = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 4])
    twopairs    = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 3])
    onepairs    = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 2])
    highcards   = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 1])

    sorted_list = highcards + onepairs + twopairs + threekinds + fullhouses + fourkinds + fivekinds

    rank = {}
    for item in sorted_list:
        rank[item] = input_data[item]

    return rank


def part1():
    data = process_input_data(r"advent of code\2023\day 7\input.txt")
    ranked_hands = sort_hands(data)

    total_winnings = 0
    for i, hand in enumerate(ranked_hands):
        rank = i + 1
        bid = data[hand]
        total_winnings = total_winnings + (rank * bid)

    print(f"Part 1: {total_winnings}")


def p2_get_relative_strength(char: str):
    ranking = "AKQT98765432J"
    if char not in ranking:
        exit()
    else:
        pos = ranking.find(char)
        relative_strength = len(ranking) - pos
    return relative_strength


def p2_evaluate_hand(hand: str):
    if len(hand) != 5:
        exit()

    num_jokers = get_num_occurences("J", hand)

    max_occurence = 0
    char_to_replace = ""
    for char in hand:
        occurence = get_num_occurences(char, hand)
        if occurence >= max_occurence and num_jokers > 0:
            max_occurence = occurence
            char_to_replace = char

    new_hand = hand.replace("J", char_to_replace)

    if five_of_a_kind(new_hand):
        return 7
    elif four_of_a_kind(new_hand):
        return 6
    elif full_house(new_hand):
        return 5
    elif three_of_a_kind(new_hand):
        return 4
    elif two_pair(new_hand):
        return 3
    elif one_pair(new_hand):
        return 2
    elif high_card(new_hand):
        return 1
    else:
        return None

def part2():
    data = process_input_data(r"advent of code\2023\day 7\input.txt")
    def p2_sort_hands(data):
        strength_dict = {}
        for i, hand in enumerate(list(data.keys())):
            strength = p2_evaluate_hand(hand)
            strength_dict[hand] = strength

        fivekinds   = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 7])
        fourkinds   = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 6])
        fullhouses  = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 5])
        threekinds  = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 4])
        twopairs    = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 3])
        onepairs    = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 2])
        highcards   = break_ties([x for x in strength_dict.keys() if strength_dict[x] == 1])

        sorted_list = highcards + onepairs + twopairs + threekinds + fullhouses + fourkinds + fivekinds

        rank = {}
        for item in sorted_list:
            rank[item] = data[item]

        return rank

    ranked_hands = p2_sort_hands(data)

    total_winnings = 0
    for i, hand in enumerate(ranked_hands):
        rank = i + 1
        bid = data[hand]
        total_winnings = total_winnings + (rank * bid)

    print(f"Part 2: {total_winnings}")


if __name__ == "__main__":
    part1()
    part2()
