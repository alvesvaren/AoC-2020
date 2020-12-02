import aoc
import re

data = aoc.get_input(2).splitlines()

count1 = 0
count2 = 0

for password in data:
    minc, maxc, letter, passwd = re.match(
        r"(\d+)-(\d+) ([a-z]): ([a-z]+)", password).groups()
    minc, maxc = int(minc), int(maxc)

    if passwd.count(letter) >= minc and passwd.count(letter) <= maxc:
        count1 += 1

    if ((passwd[minc-1] == letter) is not (passwd[maxc-1] == letter)):
        count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)
