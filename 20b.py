## Cleaned up version of part 1 from day 20

from collections import defaultdict
import aoc
data = aoc.get_input(20).split("\n\n")


def get_lines(tile) -> tuple[tuple[bool, ...]]:
    lines = [
        tile[0], tile[-1],
        [line[0] for line in tile],
        [line[-1] for line in tile]]
    return tuple(map(tuple, lines + [i[::-1] for i in lines]))


tiles: dict[int, list[list[bool]]] = {}
for block in data:
    bid = 0
    for y, line in enumerate(block.splitlines()):
        if y == 0:
            bid += int(line[5:-1])
            tiles.update({bid: []})
            continue
        tiles[bid].append([])
        for x, char in enumerate(line):
            tiles[bid][y-1].append(True if char == "#" else False)


shares_edge = defaultdict(set)
for bid1, tile1 in tiles.items():
    for bid2, tile2 in tiles.items():
        if bid1 == bid2:
            continue
        if len(set(get_lines(tile1)) & set(get_lines(tile2))) >= 1:
            shares_edge[bid1].add(bid2)
            shares_edge[bid2].add(bid1)
sum1 = 1
for bid, _ in filter(lambda x: len(x[1]) == 2, shares_edge.items()):
    sum1 *= bid
print("Part 1:", sum1)
