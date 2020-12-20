from collections import defaultdict

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

print()

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

sum1 = 1
for bid in map(lambda x: x[0], filter(lambda x: len(x[1]) == 2, things.items())):
    sum1 *= bid

print("Part 1:", sum1)

print(things)
ordered_things = []

