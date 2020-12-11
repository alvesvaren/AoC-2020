import aoc
from copy import copy

data = aoc.get_input(11).splitlines()

offsets = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1)
]

seatmap = {}
maxx, maxy = 0, 0
for y, line in enumerate(data):
    maxy = y + 1
    for x, char in enumerate(line):
        seatmap[x, y] = char
        maxx = x + 1
prev_state = copy(seatmap)


def get_around(x: int, y: int) -> int:
    adjacent_count = 0
    for offset in offsets:
        try:
            if prev_state[x + offset[0], y + offset[1]] == "#":
                adjacent_count += 1
        except KeyError:
            continue
    return adjacent_count


def get_visible(x: int, y: int) -> int:
    visible_count = 0
    for offset in offsets:
        for i in range(1, max(maxx, maxy)):
            current_offset = offset[0] * i, offset[1] * i
            try:
                value = prev_state[x + current_offset[0], y + current_offset[1]]
            except KeyError:
                break
            if value == "#":
                visible_count += 1
                break
            elif value == "L":
                break
    return visible_count


def step(visibility_method, maxcount) -> bool:
    anything_changed = False
    for y in range(maxy):
        for x in range(maxx):
            if prev_state[x, y] == "L" and visibility_method(x, y) == 0:
                seatmap[x, y] = "#"
                anything_changed = True
            elif prev_state[x, y] == "#" and visibility_method(x, y) >= maxcount:
                seatmap[x, y] = "L"
                anything_changed = True
    return anything_changed


seatmap_copy = copy(seatmap)
while step(get_around, 4):
    prev_state = copy(seatmap)

count1 = 0
for y in range(maxy):
    for x in range(maxx):
        if seatmap[x, y] == "#":
            count1 += 1

seatmap = seatmap_copy
while step(get_visible, 5):
    prev_state = copy(seatmap)

count2 = 0
for y in range(maxy):
    for x in range(maxx):
        if seatmap[x, y] == "#":
            count2 += 1

print("Part 1:", count1)
print("Part 2:", count2)
