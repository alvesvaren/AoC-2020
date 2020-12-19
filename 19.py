from typing import Generator, Pattern, TypeVar, Union
import aoc
import regex as re
from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(20000)

raw_rules, data = aoc.get_input(19).split("\n\n")
rules = defaultdict(list)


def recurse_rules(num: int, part2: bool) -> str:

    base = rules[num]
    if type(base[0][0]) == str:
        return str(base[0][0])
    regex = r"("
    for part in base:
        regex += r"("
        if part2 and num == 8:
            regex += r"("
        for subpart in part:
            regex += recurse_rules(int(subpart), part2)
        if part2 and num == 8:
            # [(42,), (42, 8)]
            return recurse_rules(42, part2) + r"+"
        if part2 and num == 11:
            # [(42, 31), (42, 11, 31)]
            r31 = recurse_rules(31, part2)
            r42 = recurse_rules(42, part2)
            first_part = r"(" + r42 + r31 + r")"
            return first_part + r"|" + r42 + r"(?R)" + r31
        regex += r")|"
    return regex[:-1] + r")"


for i, rule in enumerate(raw_rules.splitlines()):
    i, rule = rule.split(": ")
    i = int(i)
    parts = rule.split(" | ")
    for part in parts:
        if part == "":
            continue
        donepart = []
        for subpart in part.split(" "):
            try:
                donepart.append(int(subpart))
            except:
                donepart.append(subpart.replace('"', ""))
        rules[i].append(tuple(donepart))

meta_rule = recurse_rules(0, False)
count1, count2 = 0, 0
messages = data.splitlines()
for message in messages:
    if re.fullmatch(meta_rule, message):
        count1 += 1

meta_rule = recurse_rules(0, True)

for message in messages:
    if re.fullmatch(meta_rule, message):
        count2 += 1

print(count1)
print(count2)
