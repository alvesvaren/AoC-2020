from collections import defaultdict
import aoc

parents = defaultdict(set)
children = defaultdict(list)
data = aoc.get_input(7).splitlines()
for rule in data:
    rule = rule.replace(".", "").replace(" bags", "").replace(" bag", "")
    subj, other = rule.split(" contain ")
    contains = [bag.split(" ", 1) for bag in other.split(", ")]
    for count, color in contains:
        try:
            count = int(count)
        except ValueError:
            continue
        children[subj].append((count, color))
        parents[color].add(subj)


def recurse_gold(value="shiny gold", contains_gold=set()):
    contains_gold.add(value)
    for color in parents[value]:
        recurse_gold(color, contains_gold)
    return len(contains_gold)


def recurse_find_inner(value="shiny gold"):
    total_count = 0
    for count, color in children[value]:
        total_count += count * recurse_find_inner(color) + count
    return total_count


print(recurse_gold())
print(recurse_find_inner())
