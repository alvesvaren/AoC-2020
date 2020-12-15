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
        yield _num
        index += 1
    while index <= max_num:
        if len(spoken[num]) <= 1:
            num = 0
        else:
            num = spoken[num][-1] - spoken[num][-2]
        spoken[num].append(index)
        yield num
        index += 1

print(tuple(gen_numbers(2020))[-1])
print(tuple(gen_numbers(30000000))[-1])