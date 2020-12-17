import aoc
from copy import copy
from operator import itemgetter
from collections import defaultdict

data = aoc.get_input(17).splitlines()

space3d = defaultdict(bool)
space4d = defaultdict(bool)

offsets3d = []
offsets4d = []
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            for w in range(-1, 2):
                offsets4d.append((x, y, z, w))
            offsets3d.append((x, y, z))
offsets3d.remove((0, 0, 0))
offsets4d.remove((0, 0, 0, 0))


for y, line in enumerate(data):
    for x, char in enumerate(line):
        val = True if char == "#" else False
        space3d[x, y, 0] = val
        space4d[x, y, 0, 0] = val
prev_space3d = copy(space3d)
prev_space4d = copy(space4d)


def get_maxes(four: bool):
    space = space4d if four else space3d
    maxx = max(space.keys(), key=itemgetter(0))[0] + 1
    maxy = max(space.keys(), key=itemgetter(1))[1] + 1
    maxz = max(space.keys(), key=itemgetter(2))[2] + 1
    thing = maxx, maxy, maxz
    if four:
        maxw = max(space.keys(), key=itemgetter(3))[3] + 1
        thing = *thing, maxw
    return thing


def get_mins(four: bool):
    space = space4d if four else space3d
    minx = min(space.keys(), key=itemgetter(0))[0]
    miny = min(space.keys(), key=itemgetter(1))[1]
    minz = min(space.keys(), key=itemgetter(2))[2]
    thing = minx, miny, minz
    if four:
        minw = min(space.keys(), key=itemgetter(3))[3]
        thing = *thing, minw
    return thing


def get_cubes4d(x, y, z, w) -> int:
    count = 0
    for offset in offsets4d:
        if prev_space4d[x+offset[0], y+offset[1], z+offset[2], w+offset[3]]:
            count += 1
    return count


def get_cubes3d(x, y, z) -> int:
    count = 0
    for offset in offsets3d:
        if prev_space3d[x+offset[0], y+offset[1], z+offset[2]]:
            count += 1
    return count


def step3d(maxstep=6):
    global prev_space3d
    for step in range(maxstep):
        prev_space3d = copy(space3d)
        maxx, maxy, maxz = get_maxes(False)
        minx, miny, minz = get_mins(False)
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


def step4d(maxstep=6):
    global prev_space4d
    for step in range(maxstep):
        prev_space4d = copy(space4d)
        maxx, maxy, maxz, maxw = get_maxes(True)
        minx, miny, minz, minw = get_mins(True)
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
