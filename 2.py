import aoc
import re

data = aoc.get_input(2).splitlines()

count1 = 0
count2 = 0
for password in data:
    minc, maxc, letter, passwd = match = re.match(
        r"(\d+)-(\d+) ([a-z]): ([a-z]+)", password
    ).groups()
    if passwd.count(letter) >= int(minc) and passwd.count(letter) <= int(maxc):
        count1 += 1
    if ((passwd[int(minc)-1] == letter) or (passwd[int(maxc)-1] == letter)) \
            and not ((passwd[int(minc)-1] == letter) and (passwd[int(maxc)-1] == letter)):
        count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)
