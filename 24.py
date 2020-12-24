from operator import itemgetter
import aoc
from collections import defaultdict
from pprint import pprint

data = aoc.get_input(24).splitlines()

parsed_data: list[list] = []
should_continue = False
for line in data:
    parsed_data.append([])
    should_continue = False
    for char,next_char in zip(line, line[1:] + "_"):
        if should_continue:
            should_continue = False
            continue
        if char in "sn":
            parsed_data[-1].append(char + next_char)
            should_continue = True
        else:
            parsed_data[-1].append(char)

tiles = defaultdict(bool)
for line in parsed_data:
    # print(",".join(line), end="   ")
    x,y = 0,0
    for instruction in line:
        if instruction == "e":
            # x,y = x+1,y+1
            x += 1
            y += 1
        if instruction == "se":
            y += 1
        if instruction == "sw":
            x -= 1
        if instruction == "w":
            x -= 1
            y -= 1
        if instruction == "nw":
            y -= 1
        if instruction == "ne":
            x += 1
    tiles[x,y] = not tiles[x,y]
    # print(tiles[x,y], x,y)

prev_tiles = tiles.copy()

def get_minmax():
    minx = min(tiles.keys(), key=itemgetter(0))[0]
    miny = min(tiles.keys(), key=itemgetter(1))[1]
    maxx = max(tiles.keys(), key=itemgetter(0))[0]
    maxy = max(tiles.keys(), key=itemgetter(1))[1]
    return minx, miny, maxx, maxy

offsets = [
    (1,1),
    (0,1),
    (-1,0),
    (-1,-1),
    (0,-1),
    (1,0)
]

def get_near_tiles(x: int, y: int):
    count = 0
    for offset in offsets:
        if prev_tiles[x+offset[0],y+offset[1]]:
            count += 1
    return count

def step(maxstep: int = 100):
    global prev_tiles
    for _ in range(maxstep):
        prev_tiles = tiles.copy()
        minx, miny, maxx, maxy = get_minmax()
        for x in range(minx - 2, maxx + 2):
            for y in range(miny - 2, maxy + 2):
                tile = prev_tiles[x,y]
                near_tiles = get_near_tiles(x,y)
                if tile and near_tiles not in (1,2):
                    tiles[x,y] = False
                if not tile and near_tiles == 2:
                    tiles[x,y] = True
    return sum(tiles.values())



sum1 = 0
for value in tiles.values():
    if value % 2:
        sum1 += 1


print("Part 1:", sum1)
print("Part 2:", step())