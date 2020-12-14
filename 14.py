import aoc
import re
from collections import defaultdict

data = *map(lambda x: x.split(" = "), aoc.get_input(14).splitlines()),

mem1, mem2 = defaultdict(int), defaultdict(int)
mask = ""
for instruction,value in data:
    if instruction.startswith("mem"):
        address = int(re.split("[\[\]]", instruction)[1])
        value = int(value)
        print(instruction, value)
        value |= int(mask.replace("X", "0"), 2)
        value &= int(mask.replace("X", "1"), 2)
        mem1[address] = int(value)
    elif instruction == "mask":
        mask = value

print(sum(mem1.values()))