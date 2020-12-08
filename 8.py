import aoc
import re

data = [line.split(" ") for line in aoc.get_input(8).splitlines()]


def step():
    index = 0
    acc = 0
    ran_instuctions = set()

    while 1:
        try:
            instruction, value = tuple(data[index])
        except IndexError:
            return (True, acc)
        value = int(value)
        if index in ran_instuctions or index > len(data):
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
index = 0
acc2 = 0
while not found_thing:
    flip_instruction(index)
    acc = step()
    flip_instruction(index)
    if acc[0]:
        acc2 = acc[1]
        break
    else:
        index += 1

print("Part 1:", step()[1])
print("Part 2:", acc2)