from collections import defaultdict
from operator import itemgetter
import aoc

data = aoc.get_input(17).splitlines()

space3d: defaultdict[
    tuple[int, int, int], bool
] = defaultdict(bool)
space4d: defaultdict[
    tuple[int, int, int, int], bool
] = defaultdict(bool)

offsets3d = set()
offsets4d = set()
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            for w in range(-1, 2):
                offsets4d.add((x, y, z, w))
            offsets3d.add((x, y, z))
offsets3d.remove((0,)*3)
offsets4d.remove((0,)*4)


for y, line in enumerate(data):
    for x, char in enumerate(line):
        val = char == "#"
        space3d[x, y, 0] = val
        space4d[x, y, 0, 0] = val
prev_space3d = space3d.copy()
prev_space4d = space4d.copy()


def get_maxes(four: bool) -> tuple[int, ... ]:
    keys = (space4d if four else space3d).keys()
    maxx = max(keys, key=itemgetter(0))[0] + 1
    maxy = max(keys, key=itemgetter(1))[1] + 1
    maxz = max(keys, key=itemgetter(2))[2] + 1
    thing = maxx, maxy, maxz
    if four:
        maxw = max(keys, key=itemgetter(3))[3] + 1
        thing = *thing, maxw
    return thing


def get_mins(four: bool) -> tuple[int, ... ]:
    keys = (space4d if four else space3d).keys()
    minx = min(keys, key=itemgetter(0))[0]
    miny = min(keys, key=itemgetter(1))[1]
    minz = min(keys, key=itemgetter(2))[2]
    thing = minx, miny, minz
    if four:
        minw = min(keys, key=itemgetter(3))[3]
        thing = *thing, minw
    return thing


def get_cubes4d(x: int, y: int, z: int, w: int) -> int:
    count = 0
    for offset in offsets4d:
        if prev_space4d[
                x+offset[0],
                y+offset[1],
                z+offset[2],
                w+offset[3]]:
            count += 1
    return count


def get_cubes3d(x: int, y: int, z: int) -> int:
    count = 0
    for offset in offsets3d:
        if prev_space3d[
                x+offset[0],
                y+offset[1],
                z+offset[2]]:
            count += 1
    return count


def step3d(maxstep: int = 6):
    global prev_space3d
    for _ in range(maxstep):
        prev_space3d = space3d.copy()
        minx, miny, minz = get_mins(False)
        maxx, maxy, maxz = get_maxes(False)
        for x in range(minx - 1, maxx + 1):
            for y in range(miny - 1, maxy + 1):
                for z in range(minz - 1, maxz + 1):
                    cube = prev_space3d[x, y, z]
                    cubes = get_cubes3d(x, y, z)
                    if cube and not cubes in (2, 3):
                        space3d[x, y, z] = False
                    if not cube and cubes == 3:
                        space3d[x, y, z] = True
    return sum(space3d.values())


def step4d(maxstep: int = 6):
    global prev_space4d
    for _ in range(maxstep):
        prev_space4d = space4d.copy()
        minx, miny, minz, minw = get_mins(True)
        maxx, maxy, maxz, maxw = get_maxes(True)
        for x in range(minx - 1, maxx + 1):
            for y in range(miny - 1, maxy + 1):
                for z in range(minz - 1, maxz + 1):
                    for w in range(minw - 1, maxw + 1):
                        cube = prev_space4d[x, y, z, w]
                        cubes = get_cubes4d(x, y, z, w)
                        if cube and not cubes in (2, 3):
                            space4d[x, y, z, w] = False
                        if not cube and cubes == 3:
                            space4d[x, y, z, w] = True
    return sum(space4d.values())


print("Part 1:", step3d())
print("Part 2:", step4d())
