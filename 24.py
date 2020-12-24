from collections import defaultdict
from operator import itemgetter
import aoc

data = aoc.get_input(24).splitlines()

parsed_data: list[list[str]] = []
should_continue = False
for line in data:
    parsed_data.append([])
    should_continue = False
    for char, next_char in zip(line, line[1:] + " "):
        if should_continue:
            should_continue = False
            continue
        if char in "sn":
            char += next_char
            should_continue = True
        parsed_data[-1].append(char)


# Coordinate system:
#        / \     / \
#      /     \ /     \
#     |  0,-1 |  1,0  |
#     |  nw   |  ne   |
#    / \     / \     / \
#  /     \ /     \ /     \
# | -1,-1 |  0,0  |  1,1  |
# |   w   |  ref  |   e   |
#  \     / \     / \     /
#    \ /     \ /     \ /
#     | -1,0  |  0,1  |
#     |  sw   |  se   |
#      \     / \     /
#        \ /     \ /

offsets = {
    "e": (1, 1),
    "se": (0, 1),
    "sw": (-1, 0),
    "w": (-1, -1),
    "nw": (0, -1),
    "ne": (1, 0)
}


tiles = defaultdict(bool)
for line in parsed_data:
    x, y = 0, 0
    for instruction in line:
        offset = offsets[instruction]
        x, y = x+offset[0], y+offset[1]
    tiles[x, y] = not tiles[x, y]


def get_minmax():
    minx = min(tiles.keys(), key=itemgetter(0))[0]
    miny = min(tiles.keys(), key=itemgetter(1))[1]
    maxx = max(tiles.keys(), key=itemgetter(0))[0]
    maxy = max(tiles.keys(), key=itemgetter(1))[1]
    return minx, miny, maxx, maxy


def get_near_tiles(x: int, y: int):
    count = 0
    for offset in offsets.values():
        if prev_tiles[x+offset[0], y+offset[1]]:
            count += 1
    return count


def step(maxstep: int = 100):
    global prev_tiles
    for _ in range(maxstep):
        prev_tiles = tiles.copy()
        minx, miny, maxx, maxy = get_minmax()
        for x in range(minx - 2, maxx + 2):
            for y in range(miny - 2, maxy + 2):
                tile = prev_tiles[x, y]
                near_tiles = get_near_tiles(x, y)
                if tile and near_tiles not in (1, 2):
                    tiles[x, y] = False
                if not tile and near_tiles == 2:
                    tiles[x, y] = True
    return sum(tiles.values())


print("Part 1:", sum(tiles.values()))
print("Part 2:", step())
