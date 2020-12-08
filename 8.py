import aoc
import re

data = [line.split(" ") for line in aoc.get_input(8).splitlines()]


def step(allow_infinite_loops = True, verbose = False):
    index = 0
    acc = 0
    ran_instuctions = set()

    while 1:
        try:
            instruction, value = tuple(data[index])
        except IndexError:
            return (True, acc)
        if verbose:
            print(f"{instruction} {value}, i={index} acc={acc}")
        value = int(value)
        if (index in ran_instuctions and not allow_infinite_loops) \
            or index > len(data):
            return (index > len(data), acc)
        else:
            ran_instuctions.add(index)
        if instruction == "nop":
            pass
        elif instruction == "acc":
            acc += value
        elif instruction == "jmp":
            index += value
            continue
        
        
        index += 1

def flip_instruction(index):
    if data[index][0] == "nop":
        data[index][0] = "jmp"
    elif data[index][0] == "jmp":
        data[index][0] = "nop"

found_thing = False
index_to_change = 0
while not found_thing:
    flip_instruction(index_to_change)
    acc = step(False)
    print(acc)
    if acc[0]:
        print("ACCC", acc[1])
        quit()
    else:
        flip_instruction(index_to_change)
        index_to_change += 1

print(step(False)[1])
# print(step(True, True))