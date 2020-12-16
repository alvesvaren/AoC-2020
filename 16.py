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
# field_indexes = defaultdict(lambda: defaultdict(int))
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

for key,value in works_for_index.items():
    thing = list(value)
    for item in thing:
        works_for_index[key].discard(item)
        works_for_index[key].add(item[0])

used = set()

while any([len(i) > 1 for i in works_for_index.values()]):
    # print([len(i) > 1 for i in works_for_index.items()])
    for key,i in works_for_index.items():
        if len(i) == 1:
            used.add(next(iter(i)))
        if len(i) > 1:
            # print (used)
            works_for_index[key] = (i | used) ^ used
        # print(works_for_index)

order = list(next(iter(i)) for i in works_for_index.values())

ans = 1
for i,item in enumerate(order):
    if item.startswith("departure"):
        ans *= your[i]

print(ans)

# fucked = set()
# def recurse_order(order):
#     if len(order) == len(rules):
#         return order
#     pos = works_for_index[len(order)]
#     for name in pos:
#         print(name)
#         if tuple(order) not in fucked:
#             return recurse_order(order + [name])
#     fucked.add(tuple(order))
#     return recurse_order(order[:-1])

# while 1:
#     order = recurse_order([])
#     if list(set(sorted(order))) == sorted(order):
#         print(order)
#         break

# print(recurse_order([]))

# fucked = set()
# def recurse_order(order):
#     if len(order) == len(rules):
#         return order
#     used = set(order)
#     print(used)
#     for name in new_rules.keys():
#         if tuple(order + [name]) in fucked:
#             continue
#         if name not in used and name in works_for_index[len(order)]:
#             # fucked.clear()
#             return recurse_order(order + [name])
#     fucked.add(tuple(order))
#     return recurse_order([])


# try:
#     print(recurse_order([]))
# except RecursionError:
#     print("Recursion error")
#     quit()


# ans = 1
# for i,item in enumerate(recurse_order([])):
#     if not item.startswith("departure"):
#         continue
#     ans *= your[i]
# print(ans)
# print(works_for_index)

# possible_fields = defaultdict(set)

# for i in range(len(rules)):
#     for j in new_rules.values():
#         for rule in j:
#             possible_fields[i].add(rule)

# print(possible_fields)


# for ticket in valid_tickets:
#     for index, field in enumerate(ticket):
#         for name, ranges in new_rules.items():
#             for rule in ranges:
#                 if not field in rule:
#                     print(field, rule)
#                     possible_fields[index].discard(rule)

# print(possible_fields)


# for i in sorted(works_for_index, key=lambda x: len(works_for_index[x])):
#     this = next(iter(works_for_index[i]))
#     for j in works_for_index:
#         if i != j:
#             works_for_index[i].discard(this)

# print(works_for_index)

# print(new_rules)

# possible_fields = {i: set(chain.from_iterable(i for i in new_rules.values())) for i in range(len(rules) + 1)}

# for ticket in valid_tickets:
#     for i, value in enumerate(ticket):
#         for fields in new_rules.values():
#             for field in fields:
#                 if not value in field:
#                     possible_fields[i].discard(field)
#                 else:
#                     break

# for i in sorted(possible_fields, key=lambda x: len(possible_fields[x])):
#     this_field = next(iter(possible_fields[i]))
#     for j in possible_fields:
#         if i != j:
#             possible_fields[j].discard(this_field)
# # print(possible_fields)

# print(your)

# ans = 1
# for name,rule in new_rules.items():
#     if not name.startswith("departure"):
#         continue
#     for index,thing in possible_fields.items():
#         if next(iter(thing)) in rule:
#             ans *= your[index]


# 6595721127277
# print(ans)

# possible_fields = defaultdict(set)
# chain.from_iterable(new_rules.values())
# 2587271823407 !!!
# for index in can_be.items():

#     print(index)

# for ticket in valid_tickets:
#     for index,field in enumerate(ticket):
#         for name,ranges in new_rules.items():
#             for rule in ranges:
#                 if field in rule:
#                     field_indexes[name][index] += 1

# has = defaultdict(set)
# missing = defaultdict(set)
# for name, thing in field_indexes.items():
#     for index, value in thing.items():
#         if value != len(valid_tickets):
#             missing[name].add(index)
#             continue
#         has[name].add(index)
#     print(has[name] > missing[name])


# while 1:
#     for i in range(20):
#         valid = [j for j in range(20) if ]



# for combination in permutations(new_rules):
#     all_matches = True
#     for index, name1 in enumerate(combination):
#         for name2,things in new_rules.items():
#             if not name1 == name2:
#                 continue
#             for possible in field_indexes.values():
#                 print(possible)
#                 if not (possible == len(rules)):
#                     all_matches = False
#     if all_matches:
#         print(combination)
#         break
# real_combination = None
# count = 0


# for combination in permutations(new_rules):
#     all_matches = True
#     count += 1
#     if count % 10000 == 0:
#         print(count)
#     for index,name1 in enumerate(combination):
#         if not name1.startswith("departure "):
#             continue
#         for name2,indexes in field_indexes.items():
#             if not name1 == name2:
#                 continue
#             if not (indexes[index] == len(rules)):
#                 all_matches = False
#                 # print(name1, index, indexes.items())
#     if all_matches:
#         real_combination = combination
#         break
# print(real_combination)
# for index,value in enumerate(real_combination):
#     print(your)

print("Part 1:", count1)
