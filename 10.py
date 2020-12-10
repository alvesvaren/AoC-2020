import aoc
from functools import lru_cache
from collections import defaultdict

data = *map(int, aoc.get_input(10).splitlines()),

differences = defaultdict(int)
data = sorted((0,) + data + (max(data)+3,))
for adapter, other_adapter in zip(data, data[1:]):
    differences[abs(other_adapter - adapter)] += 1


@lru_cache
def count_combinations(start):
    if start == data[-1]:
        return 1
    count = 0
    for i in 1, 2, 3:
        if start + i not in data:
            continue
        count += count_combinations(start + i)
    return count


print("Part 1:", differences[1] * differences[3])
print("Part 2:", count_combinations(data[0]))
