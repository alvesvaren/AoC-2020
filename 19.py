from typing import Generator, Pattern, TypeVar, Union
import aoc
import re
from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(20000)

raw_rules, data = aoc.get_input(19).split("\n\n")
rules = defaultdict(list)

def recurse_rules(num: int) -> Union[re.Pattern, str]:
    
    base = rules[num]
    print(base, num)
    if type(base[0][0]) == str:
        return str(base[0][0])
    regex = r"("
    for part in base:
        regex += r"("
        for subpart in part:
            regex += recurse_rules(int(subpart))
        regex += r")|"
    return regex[:-1] + r")"

for i, rule in enumerate(raw_rules.splitlines()):
    i, rule = rule.split(": ")
    i = int(i)
    parts = rule.split(" | ")
    for part in parts:
        if part == "":
            continue
        # print(part)
        donepart = []
        for subpart in part.split(" "):
            try:
                donepart.append(int(subpart))
            except:
                donepart.append(subpart.replace('"', ""))
        rules[i].append(tuple(donepart))

meta_rule = recurse_rules(0)

count1 = 0
messages = data.splitlines()
for message in messages:
    if re.fullmatch(meta_rule, message):
        count1 += 1
print(count1)
