import aoc
from itertools import permutations

data = *map(int, aoc.get_input(9).splitlines()),

length = 25
for start in range(length, len(data)):
    to_sum = data[start]
    any_matches = False
    for num1 in data[start-length:start]:
        for num2 in data[start-length:start]:
            if num1+num2 == to_sum and num1 != num2:
                any_matches = True
                

    if not any_matches:
        print(to_sum)
        break