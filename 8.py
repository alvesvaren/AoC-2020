import aoc

data = *map(str.split, aoc.get_input(8).splitlines()),


def step():
    index = 0
    acc = 0
    ran_instuctions = set()

    while 1:
        if index >= len(data):
            return (True, acc)
        instruction, value = tuple(data[index])
        value = int(value)
        if index in ran_instuctions:
            return (False, acc)
        ran_instuctions.add(index)
        if instruction == "acc":
            acc += value
        elif instruction == "jmp":
            index += value
            continue
        index += 1


def flip(index):
    if data[index][0] == "nop":
        data[index][0] = "jmp"
    elif data[index][0] == "jmp":
        data[index][0] = "nop"


acc2 = 0
for index in range(len(data)):
    flip(index)
    acc = step()
    flip(index)
    if acc[0]:
        acc2 = acc[1]
        break

print("Part 1:", step()[1])
print("Part 2:", acc2)
