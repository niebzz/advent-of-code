from utilities.web import get_puzzle_input


def get_initial_signals(data: list[str], wires: dict):
    operators = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
    for line in data:
        operator = [x for x in operators if x in line.split(" ")]
        if len(operator) == 0:
            signal, output_wire = line.split(" -> ")
            try:
                wires[output_wire] = int(signal)
            except:
                pass
    return


def assign_signal(line: str, wires: dict):
    operators = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
    operator = [x for x in operators if x in line.split(" ")]
    output_wire = line.split(" ")[-1]
    num_bits = 2 ** 16

    if wires[output_wire] != None:
        return

    match operator:
        case ["RSHIFT"]:
            input_wire = line.split(" ")[0]
            input_signal = wires[input_wire]
            if input_signal is None:
                return
            else:
                bit1, bit2 = input_signal, int(line.split(" ")[2])
                wires[output_wire] = (bit1 >> bit2) % num_bits
                return

        case ["LSHIFT"]:
            input_wire = line.split(" ")[0]
            input_signal = wires[input_wire]
            if input_signal is None:
                return
            else:
                bit1, bit2 = input_signal, int(line.split(" ")[2])
                wires[output_wire] = (bit1 << bit2) % num_bits
                return

        case ["NOT"]:
            input_wire = line.split(" ")[1]
            input_signal = wires[input_wire]
            if input_signal is None:
                return
            else:
                wires[output_wire] = ~input_signal % num_bits
                return

        case ["AND"]:
            input_wire1, input_wire2 = line.split(" ")[0], line.split(" ")[2]
            try:
                input_signal1 = wires[input_wire1]
            except KeyError:
                input_signal1 = int(input_wire1)
            input_signal2 = wires[input_wire2]

            if input_signal1 == None or input_signal2 == None:
                return
            else:
                wires[output_wire] = (input_signal1 & input_signal2) % num_bits
                return

        case ["OR"]:
            input_wire1, input_wire2 = line.split(" ")[0], line.split(" ")[2]
            input_signal1, input_signal2 = wires[input_wire1], wires[input_wire2]

            if input_signal1 == None or input_signal2 == None:
                return
            else:
                wires[output_wire] = (input_signal1 | input_signal2) % num_bits
                return


def part1(data):
    wires = {line.split(" -> ")[1]: None for line in data}
    get_initial_signals(data, wires)

    while wires["lx"] == None:  # lx -> a
        for line in data:
            assign_signal(line, wires)

    wires["a"] = wires["lx"]

    return wires["a"]


def main():
    data = get_puzzle_input(year=2015, day=7).strip().split("\n")
    p1 = part1(data)
    print(f"Part 1: {p1}")

    data[54] = str(p1) + " -> b"  # row 54 is where 'b' is defined
    p2 = part1(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
