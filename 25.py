import aoc
from itertools import count

num1, num2 = *map(int, aoc.get_input(25).splitlines()),
some_numbers = (
    77, 101, 114, 114,
    121, 32, 67, 104,
    114, 105, 115, 116,
    109, 97, 115, 33
)

i = 0
subj = 1
for i in count(start=1):
    subj *= 7
    subj %= 20201227
    if subj == num2:
        break


sum1 = 1
for i in range(i):
    sum1 *= num1
    sum1 %= 20201227

print("Part 1:", sum1)
print("Part 2:", "".join(map(chr, some_numbers)))
