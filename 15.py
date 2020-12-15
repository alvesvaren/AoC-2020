import aoc
from copy import copy
from collections import defaultdict

data = *map(int,aoc.get_input(15).split(",")),

def gen_numbers(max_num):
    start = iter(data)
    spoken = defaultdict(list)
    num = 0
    index = 1
    for _num in start:
        num = _num
        spoken[num].append(index)
        index += 1
    while index <= max_num:
        if len(spoken[num]) <= 1:
            num = 0
        else:
            num = spoken[num][-1] - spoken[num][-2]
        spoken[num].append(index)
        index += 1
    return num

print("Part 1:", gen_numbers(2020))
print("Part 2:", gen_numbers(30000000))