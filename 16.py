import aoc
import re
from collections import defaultdict
from itertools import chain

rules, your, nearby = aoc.get_input(16).split("\n\n")

your = re.split(r"[\n,]", your.split("\n", 1)[1])
nearby = [i.split(",") for i in nearby.split("\n")[1:]]
nearby = [(*map(int, i),) for i in nearby]
print(nearby)
rules = rules.splitlines()
new_rules = defaultdict(list)
for rule in rules:
    match = re.match(r"(\w+ *\w*): (\d+)-(\d+) or (\d+)-(\d+)", rule)
    name, r1a, r1b, r2a, r2b = match.groups()
    range1 = range(int(r1a), int(r1b) + 1)
    range2 = range(int(r2a), int(r2b) + 1)
    new_rules[name].append(range1)
    new_rules[name].append(range2)

print(nearby)
count1 = 0
for ticket in nearby:
    for field in ticket:
        matches_any = False
        for rule in chain.from_iterable(new_rules.values()):
            if field in rule:
                matches_any = True
                break
        if not matches_any:
            count1 += field

print("Part 1:", count1)
