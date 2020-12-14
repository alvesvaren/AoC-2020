import aoc
import re
from itertools import permutations
from collections import defaultdict

data = *map(lambda x: x.split(" = "), aoc.get_input(14).splitlines()),

mem1, mem2 = defaultdict(int), defaultdict(int)
mask = "", ""
for instruction, value1 in data:
    if instruction.startswith("mem"):
        address1 = int(re.split("[\[\]]", instruction)[1])
        value1 = int(value1)
        value2 = value1
        flip = False

        def gen_addresses(base_mask):
            address = 0
            while 1:
                yield address
                address += 1
                address = address + ~base_mask & base_mask
                if address == 0:
                    break
        for address2 in gen_addresses(int(mask.replace("1", "0").replace("X", "1"), 2)):
            mem2[address2] = value2
        value1 |= int(mask.replace("X", "0"), 2)
        value1 &= int(mask.replace("X", "1"), 2)
        mem1[address1] = int(value1)
    elif instruction == "mask":
        mask = value1

print("Part 1:", sum(mem1.values()))
print("Part 2:", sum(mem2.values()))
