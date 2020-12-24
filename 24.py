import aoc
from collections import defaultdict
from pprint import pprint

data = aoc.get_input(24).splitlines()

parsed_data: list[list] = []
should_continue = False
for line in data:
    parsed_data.append([])
    should_continue = False
    for char,next_char in zip(line, line[1:] + "_"):
        if should_continue:
            should_continue = False
            continue
        if char in "sn":
            parsed_data[-1].append(char + next_char)
            should_continue = True
        else:
            parsed_data[-1].append(char)

tiles = defaultdict(int)
for line in parsed_data:
    # print(",".join(line), end="   ")
    x,y = 0,0
    for instruction in line:
        if instruction == "e":
            # x,y = x+1,y+1
            x += 1
            y += 1
        if instruction == "se":
            y += 1
        if instruction == "sw":
            x -= 1
        if instruction == "w":
            x -= 1
            y -= 1
        if instruction == "nw":
            y -= 1
        if instruction == "ne":
            x += 1
    tiles[x,y] += 1
    # print(tiles[x,y], x,y)

sum1 = 0
for value in tiles.values():
    if value % 2:
        sum1 += 1

print(sum1)