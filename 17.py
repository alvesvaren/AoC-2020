from requests.api import get
import aoc
from collections import defaultdict
from operator import itemgetter
from copy import copy

data = aoc.get_input(17).splitlines()

space = defaultdict(bool)

offsets = []
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            for w in range(-1, 2):
                offsets.append((x, y, z, w))
offsets.remove((0, 0, 0, 0))


for y, line in enumerate(data):
    for x, char in enumerate(line):
        space[x, y, 0, 0] = True if char == "#" else False
prev_space = copy(space)

def get_maxes():
    maxx = max(space.keys(), key=itemgetter(0))[0] + 1
    maxy = max(space.keys(), key=itemgetter(1))[1] + 1
    maxz = max(space.keys(), key=itemgetter(2))[2] + 1
    maxw = max(space.keys(), key=itemgetter(3))[3] + 1
    return maxx, maxy, maxz, maxw

def get_mins():
    minx = min(space.keys(), key=itemgetter(0))[0]
    miny = min(space.keys(), key=itemgetter(1))[1] 
    minz = min(space.keys(), key=itemgetter(2))[2]
    minw = min(space.keys(), key=itemgetter(3))[3]
    return minx, miny, minz, minw

def pretty_print_space():
    maxx, maxy, maxz = get_maxes()
    minx, miny, minz = get_mins()
    print("Max:", f"x:{maxx} y:{maxy} z:{maxz}")

    for z in range(minz, maxz):
        print(f"z={z}")
        for y in range(miny, maxy):
            for x in range(minx, maxx):
                print("#" if space[x, y, z] else ".", end="")
            print()
        print()


# pretty_print_space()


def get_cubes(x, y, z, w) -> int:
    count = 0
    for offset in offsets:
        if prev_space[x+offset[0], y+offset[1], z+offset[2], w+offset[3]]:
            count += 1
    return count


# def step3d(maxstep = 6):
#     global prev_space
#     for i in range(maxstep):
#         prev_space = copy(space)
#         maxx, maxy, maxz = get_maxes()
#         minx, miny, minz = get_mins()
#         for x in range(minx - 1, maxx + 1):
#             for y in range(miny - 1, maxy + 1):
#                 for z in range(minz - 1, maxz + 1):
#                     cube = prev_space[x,y,z]
#                     cubes = get_cubes(x,y,z)
#                     if cube and not cubes in (2,3):
#                         space[x,y,z] = False
#                     if not cube and cubes == 3:
#                         space[x,y,z] = True
#         # pretty_print_space()
#     return sum(1 if i else 0 for i in space.values())

def step4d(maxstep = 6):
    global prev_space
    for i in range(maxstep):
        prev_space = copy(space)
        maxx, maxy, maxz, maxw = get_maxes()
        minx, miny, minz, minw = get_mins()
        for x in range(minx - 1, maxx + 1):
            for y in range(miny - 1, maxy + 1):
                for z in range(minz - 1, maxz + 1):
                    for w in range(minw - 1, maxw + 1):
                        cube = prev_space[x,y,z,w]
                        cubes = get_cubes(x,y,z,w)
                        if cube and not cubes in (2,3):
                            space[x,y,z,w] = False
                        if not cube and cubes == 3:
                            space[x,y,z,w] = True
        # pretty_print_space()
    return sum(1 if i else 0 for i in space.values())

# space_copy = copy(space)
# while step():
#     prev_space = copy(space)

print(step4d())
