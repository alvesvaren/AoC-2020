import aoc
import re
from collections import defaultdict
from itertools import chain, permutations
from sys import setrecursionlimit
setrecursionlimit(20000)

rules, your, nearby = aoc.get_input(16).split("\n\n")

your = [i.split(",") for i in your.split("\n")[1:]]
your = [(*map(int, i),) for i in your][0]

nearby = [i.split(",") for i in nearby.split("\n")[1:]]
nearby = [(*map(int, i),) for i in nearby]

rules = rules.splitlines()
new_rules = defaultdict(tuple)
for rule in rules:
    match = re.match(r"(\w+ *\w*): (\d+)-(\d+) or (\d+)-(\d+)", rule)
    name, r1a, r1b, r2a, r2b = match.groups()
    range1 = range(int(r1a), int(r1b) + 1)
    range2 = range(int(r2a), int(r2b) + 1)
    new_rules[name] = (range1, range2)

invalid = set()
count1 = 0
for ticket in nearby:
    for index, field in enumerate(ticket):
        matches_any = False
        for name, ranges in new_rules.items():
            for rule in ranges:
                if field in rule:
                    matches_any = True

        if not matches_any:
            count1 += field
            invalid.add(ticket)
valid_tickets = *filter(lambda x: x not in invalid, nearby),

works_for_index = defaultdict(set)

for i in range(len(rules)):
    for rule in new_rules.items():
        works_for_index[i].add(rule)

for index in range(len(rules)):
    doesnt_work_for_index = set()
    for rule in works_for_index[index]:
        for ticket in valid_tickets:
            if not any([ticket[index] in r for r in rule[1]]):
                doesnt_work_for_index.add(rule)
    works_for_index[index] ^= doesnt_work_for_index

for key, value in works_for_index.items():
    thing = list(value)
    for item in thing:
        works_for_index[key].discard(item)
        works_for_index[key].add(item[0])

used = set()

while any([len(i) > 1 for i in works_for_index.values()]):
    for key, i in works_for_index.items():
        if len(i) > 1:
            works_for_index[key] = (i | used) ^ used
        else:
            used.add(next(iter(i)))

order = list(next(iter(i)) for i in works_for_index.values())

count2 = 1
for i, item in enumerate(order):
    if item.startswith("departure"):
        count2 *= your[i]

print("Part 1:", count1)
print("Part 2:", count2)
