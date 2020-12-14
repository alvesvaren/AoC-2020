import aoc
import re
from itertools import permutations
from collections import defaultdict

data = *map(lambda x: x.split(" = "), aoc.get_input(14).splitlines()),

mem1, mem2 = defaultdict(int), defaultdict(int)
mask = "", ""
for instruction, value in data:
    if instruction.startswith("mem"):
        address1 = int(re.split("[\[\]]", instruction)[1])
        value = int(value)

        def gen_addresses(start_address, new_mask):
            if not new_mask:
                yield 0
            else:
                for curr_address in gen_addresses(start_address//2, new_mask[:-1]):
                    current_bit = new_mask[-1]
                    curr_address *= 2
                    if current_bit == "0":
                        yield curr_address + start_address % 2
                    if current_bit in "1X":
                        yield curr_address + 1
                    if current_bit == "X":
                        yield curr_address
        for address in gen_addresses(address1, mask):
            mem2[address] = value
        value |= int(mask.replace("X", "0"), 2)
        value &= int(mask.replace("X", "1"), 2)
        mem1[address1] = int(value)
    elif instruction == "mask":
        mask = value

print("Part 1:", sum(mem1.values()))
print("Part 2:", sum(mem2.values()))
