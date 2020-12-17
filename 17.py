from requests.api import get
import aoc
from collections import defaultdict
from operator import itemgetter
from copy import copy

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
        space3d[x,y,0] = val
        space4d[x, y, 0, 0] = val
prev_space3d = copy(space3d)
prev_space4d = copy(space4d)

def get_maxes3d():
    maxx = max(space3d.keys(), key=itemgetter(0))[0] + 1
    maxy = max(space3d.keys(), key=itemgetter(1))[1] + 1
    maxz = max(space3d.keys(), key=itemgetter(2))[2] + 1
    return maxx, maxy, maxz

def get_mins3d():
    miny = min(space3d.keys(), key=itemgetter(1))[1] 
    minx = min(space3d.keys(), key=itemgetter(0))[0]
    minz = min(space3d.keys(), key=itemgetter(2))[2]
    return minx, miny, minz

def get_maxes4d():
    maxx = max(space4d.keys(), key=itemgetter(0))[0] + 1
    maxy = max(space4d.keys(), key=itemgetter(1))[1] + 1
    maxz = max(space4d.keys(), key=itemgetter(2))[2] + 1
    maxw = max(space4d.keys(), key=itemgetter(3))[3] + 1
    return maxx, maxy, maxz, maxw

def get_mins4d():
    minx = min(space4d.keys(), key=itemgetter(0))[0]
    miny = min(space4d.keys(), key=itemgetter(1))[1] 
    minz = min(space4d.keys(), key=itemgetter(2))[2]
    minw = min(space4d.keys(), key=itemgetter(3))[3]
    return minx, miny, minz, minw



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

def step3d(maxstep = 6):
    global prev_space3d
    for i in range(maxstep):
        prev_space3d = copy(space3d)
        maxx, maxy, maxz = get_maxes3d()
        minx, miny, minz = get_mins3d()
        for x in range(minx - 1, maxx + 1):
            for y in range(miny - 1, maxy + 1):
                for z in range(minz - 1, maxz + 1):
                    cube = prev_space3d[x,y,z]
                    cubes = get_cubes3d(x,y,z)
                    if cube and not cubes in (2,3):
                        space3d[x,y,z] = False
                    if not cube and cubes == 3:
                        space3d[x,y,z] = True
    return sum(1 if i else 0 for i in space3d.values())

def step4d(maxstep = 6):
    global prev_space4d
    for i in range(maxstep):
        prev_space4d = copy(space4d)
        maxx4d, maxy4d, maxz4d, maxw4d = get_maxes4d()
        minx4d, miny4d, minz4d, minw4d = get_mins4d()
        for x in range(minx4d - 1, maxx4d + 1):
            for y in range(miny4d - 1, maxy4d + 1):
                for z in range(minz4d - 1, maxz4d + 1):
                    for w in range(minw4d - 1, maxw4d + 1):
                        cube = prev_space4d[x,y,z,w]
                        cubes = get_cubes4d(x,y,z,w)
                        if cube and not cubes in (2,3):
                            space4d[x,y,z,w] = False
                        if not cube and cubes == 3:
                            space4d[x,y,z,w] = True
        # pretty_print_space()
    return sum(1 if i else 0 for i in space4d.values())

# space_copy = copy(space)
# while step():
#     prev_space = copy(space)
print("Part 1:", step3d())
print("Part 2:", step4d())
