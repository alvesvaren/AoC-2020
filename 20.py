from collections import defaultdict
from pprint import pprint
from numpy.lib.arraysetops import intersect1d
import aoc
import numpy as np
from itertools import chain

data = aoc.get_input(20).split("\n\n")

# print(len(data))


def rotate(thing: list[list], half_radian: int):
    if half_radian == 0:
        return thing
    return rotate(list(map(list, zip(*thing[::-1]))), half_radian-1)

def flip(thing: list[list], horizontal: bool = False, vertical: bool = False):
    if vertical:
        thing = thing[::-1]
    if horizontal:
        thing = list(map(lambda x: x[::-1], thing))
    return thing

# print(flip([[1,2], [3,4]]))

class Block:
    def __init__(self, id: int, grid: list[list[bool]]):
        self.id = id
        self.grid = grid

    def get_lines(self) -> list[tuple[bool, ...]]:
        things = []
        things.append(self.grid[0])
        things.append(self.grid[-1])
        things.append([line[0] for line in self.grid])
        things.append([line[-1] for line in self.grid])
        
        things.append(self.grid[0][::-1])
        things.append(self.grid[-1][::-1])
        things.append([line[0] for line in self.grid][::-1])
        things.append([line[-1] for line in self.grid][::-1])
        return list(map(tuple, things))
    
    def __repr__(self):
        string = f"Tile {self.id}:"
        for line in self.grid:
            string += "\n"
            for value in line:
                string += "#" if value else "."
        return string

blocks: list[Block] = []
for block in data:
    thing = {}
    for y,line in enumerate(block.splitlines()):
        if y == 0:
            thing = {"id": int(line[5:-1]), "grid": []}
            continue
        thing["grid"].append([])
        for x,char in enumerate(line):
            thing["grid"][y-1].append(True if char == "#" else False)
    blocks.append(Block(**thing))

# print(blockdata[0].get_lines())


edges = []
for block in blocks:
    for i,edge in enumerate(block.get_lines()):
        edges.append((block.id, edge, i))
# edges = [(block.id, block.get_lines()) for block in blocks]

# matching_edges = defaultdict(set)
# for bid,edge,i in edges:
#     if edge in map(lambda x: x[1], edges):
#         new_bid = next(filter(lambda x: x[1] == edge, edges))[0]
#         if new_bid != bid:
#             matching_edges[bid].add(new_bid)
things = defaultdict(set)
for block1 in blocks:
    for block2 in blocks:
        if block1.id == block2.id: 
            continue
        if len(set(block1.get_lines()) & set(block2.get_lines())) >= 1:
            things[block1.id].add(block2.id)
            things[block2.id].add(block1.id)
corners = set()
sum1 = 1
for bid in map(lambda x: x[0], filter(lambda x: len(x[1]) == 2, things.items())):
    sum1 *= bid
    corners.add(bid)

print("Part 1:", sum1)

# pprint(things)

edges_and_corners = list(filter(lambda x: len(x[1]) <= 3, things.items()))

grid = defaultdict(int)

grid[0,0] = next(iter(corners))
todo = edges_and_corners.copy()
todo.remove(next(filter(lambda x: x[0] == grid[0,0], todo)))

sorted_ring = [grid[0,0]]
while todo:
    next_item = next(filter(lambda x: sorted_ring[-1] in x[1], todo))
    sorted_ring.append(next_item[0])
    todo.remove(next(filter(lambda x: x[0] == sorted_ring[-1], todo)))

offsets = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def gen_offstets_forever():
    v = 0
    while 1:
        yield offsets[v]
        v += 1
        v = v % len(offsets)

def gen_xy_square_spiral(length: int):
    x,y = 0,0
    i = 0
    for offset in gen_offstets_forever():
        for _ in range(length-1):
            yield x,y
            x += offset[0]
            y += offset[1]
        i += 1
        if i % 3 == 0:
            length -= 1
        if length <= 1:
            break

def matches_adjacent(grid,x,y,adj):
    any_fails = False
    for offset in offsets:
        if grid[x+offset[0], y+offset[1]]:
            if not grid[x+offset[0], y+offset[1]] in adj:
                any_fails = True
    return not any_fails

# i = 0
grid = defaultdict(int)
grid[0,0] = next(iter(corners))
# grid[0,0] = next(iter(corners))
# remove_from_todo = [(grid[0,0], things[grid[0,0]])] + edges_and_corners
todo = [(grid[0,0], things[grid[0,0]])] + edges_and_corners + list(things.items())
# print(todo)
# print(things)



# for item in filter(lambda x: x[0] != grid[0,0], remove_from_todo):
#     # print(item)
#     todo

# # todo = remove_from_todo + todo
# print(todo)
# print(len(todo))
used = set()
for x,y in gen_xy_square_spiral(int(len(things)**.5)):
    for bid,adj in todo:
        if matches_adjacent(grid, x,y, adj) and bid not in used:
            grid[x,y] = bid
            # print(bid, adj, x,y)
            todo.remove((bid,adj))
            used.add(bid)
            break
    # grid[x,y] = sorted_ring[i]
    # i += 1
# print(things)
# print(sorted_ring)
# next(filter(lambda x: len(x[1] & {sorted_ring[0], sorted_ring[-1]}) == 2, things.items()))
for key,value in list(grid.items()):
    if value == 0:
        del grid[key]

