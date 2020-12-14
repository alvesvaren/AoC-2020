import aoc
import re
from itertools import combinations
from collections import defaultdict

data = *map(lambda x: x.split(" = "), aoc.get_input(14).splitlines()),

mem1, mem2 = defaultdict(int), defaultdict(int)
mask = ""
for instruction,value1 in data:
    if instruction.startswith("mem"):
        address = int(re.split("[\[\]]", instruction)[1])
        value1 = int(value1)
        value2 = value1
        print(instruction, value1)
        value1 |= int(mask.replace("X", "0"), 2)
        value1 &= int(mask.replace("X", "1"), 2)
        mem1[address] = int(value1)
    elif instruction == "mask":
        mask = value1

print(sum(mem1.values()))