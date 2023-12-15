import re

INPUT_FILE = r"advent of code\2023\day 15\input.txt"


def get_hash_value(ascii_string: str) -> int:
    current_value = 0
    for char in ascii_string:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


def sort_into_box(ascii_string: str, boxes: dict[list]):
    delimiter = re.findall("[-=]", ascii_string)[0]
    label = ascii_string.split(delimiter)[0]
    box_number = get_hash_value(label)
    try:
        focal_length = int(ascii_string[-1])
    except:
        focal_length = 0

    has_existing_label = True if label in boxes[box_number] else False
    is_empty_box = True if boxes[box_number] == [] else False

    if delimiter == "=":
        if not has_existing_label and is_empty_box:
            boxes[box_number] = [label, focal_length]
        elif not has_existing_label and not is_empty_box:
            inside_box = boxes[box_number]
            item_to_add = [label, focal_length]
            boxes[box_number] = inside_box + item_to_add
        elif has_existing_label:
            inside_box = boxes[box_number]
            i = inside_box.index(label)
            inside_box[i+1] = focal_length
            boxes[box_number] = inside_box
    elif delimiter == "-":
        if not has_existing_label:
            pass
        elif has_existing_label:
            inside_box = boxes[box_number]
            i = inside_box.index(label)
            del inside_box[i]
            del inside_box[i]
            boxes[box_number] = inside_box
    return boxes


def part1(input_txt):
    with open(input_txt) as f:
        data = tuple(x for x in f.read().strip().split(","))

    p1_total = sum([get_hash_value(step) for step in data])
    print(f"Part 1: {p1_total}")


def part2(input_txt):
    with open(input_txt) as f:
        data = tuple(x for x in f.read().strip().split(","))

    boxes = {}
    for i in range(256):
        boxes[i] = []

    for step in data:
        boxes = sort_into_box(step, boxes)

    p2_total = 0
    for box, slots in boxes.items():
        for i, focal_length in enumerate(slots[1::2]):
            box_number = box + 1
            slot_number = i + 1
            p2_total += (box_number * slot_number * focal_length)
    print(f"Part 2: {p2_total}")


part1(INPUT_FILE)
part2(INPUT_FILE)
