import aoc
from collections import defaultdict

data = *map(int, aoc.get_input(10).splitlines()),

differences = defaultdict(int)
data = list(sorted((0,) + data + (max(data)+3,)))
for adapter, other_adapter in zip(data, data[1:]):
    differences[abs(other_adapter - adapter)] += 1


for adapter in data:
    pass


print("Part 1:", differences[1] * differences[3])
print("Part 2:")
