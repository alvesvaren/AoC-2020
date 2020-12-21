import aoc
import re

data = aoc.get_input(2).splitlines()

count1, count2 = 0, 0

for password in data:
    minc, maxc, letter, passwd = re.match(
        r"(\d+)-(\d+) (\w): (\w+)", password).groups()
    minc, maxc = int(minc), int(maxc)

    if maxc >= passwd.count(letter) >= minc:
        count1 += 1

    if (passwd[minc-1] == letter) ^ (passwd[maxc-1] == letter):
        count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)
