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
    
    def get_strict_lines(self) -> list[tuple[bool, ...]]:
        things = []
        things.append(self.grid[0])
        things.append([line[0] for line in self.grid])
        things.append(self.grid[-1][::-1])
        things.append([line[-1] for line in self.grid][::-1])
        return list(map(tuple, things))
    
    def get_strict_lines_inverted(self) -> list[tuple[bool, ...]]:
        things = []
        things.append(self.grid[0][::-1])
        things.append([line[0] for line in self.grid][::-1])
        things.append(self.grid[-1])
        things.append([line[-1] for line in self.grid])
        return list(map(tuple, things))
    
    
    def __str__(self):
        string = f"Tile {self.id}:"
        for line in self.grid:
            string += "\n"
            for value in line:
                string += "#" if value else "."
        return string
    
    def __repr__(self):
        return "Tile " + str(self.id)
    
    def get_grid_without_borders(self):
        grid_without_border = []
        for y,line in enumerate(self.grid[1:-1]):
            grid_without_border.append([])
            for x,thing in enumerate(line[1:-1]):
                grid_without_border[y].append(thing)
        return grid_without_border
    

    def get_transforms(self):
        transforms = []

        for i in (0,1,2,3):
            rotated = rotate(self.grid, i)
            transforms.append(flip(rotated, False, False))
            transforms.append(flip(rotated, True, False))
            transforms.append(flip(rotated, True, True))
            transforms.append(flip(rotated, False, True))
        return transforms
    
    # def get_line_in_direction(self, direction: tuple[int, int]):
    #     # [0,1] 

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


# grid = defaultdict(int)

# grid[0,0] = next(iter(corners))
# todo = edges_and_corners.copy()
# todo.remove(next(filter(lambda x: x[0] == grid[0,0], todo)))

# sorted_ring = [grid[0,0]]
# while todo:
#     next_item = next(filter(lambda x: sorted_ring[-1] in x[1], todo))
#     sorted_ring.append(next_item[0])
#     todo.remove(next(filter(lambda x: x[0] == sorted_ring[-1], todo)))

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

edges_and_corners = list(filter(lambda x: len(x[1]) <= 3, things.items()))

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

# def all_transforms(thing):
#     transforms = []

#     for i in (0,1,2,3):
#         rotated = rotate(thing, i)
#         transforms.append(rotated)
#         transforms.append(flip(rotated, True, False))
#         # transforms.append(flip(rotated, True, True))
#         transforms.append(flip(rotated, False, True))
#     return transforms

new_grid: dict[tuple[int, int], Block] = dict()

for key,value in grid.items():
    new_grid[key] = next(filter(lambda x: x.id == value, blocks))


grid_size = max(grid.keys(), key=lambda x: x[0])[0]


def check_if_works_up(thing1: Block, thing2: Block):
    return thing1.get_strict_lines_inverted()[2] == thing2.get_strict_lines()[0]
    # for offset in offsets:
    #     for line1 in thing.get_strict_lines():
    #         finished_offset = x + offset[0], y + offset[1]
    #         if finished_offset[0] > 0 and finished_offset[1] > 0:
    #             for line2 in new_grid[finished_offset].get_strict_lines():
    #                 if line1 == line2:
    #                     return True
    # return False
    # for line1 in thing1.get_strict_lines():
    #     for line2 in thing2.get_strict_lines():
    #         if line1 == line2:
    #             return True
def check_if_works_left(thing1: Block, thing2: Block):
    return thing1.get_strict_lines_inverted()[3] == thing2.get_strict_lines()[1]
    # for offset in offsets:
    #     for line1 in thing.get_strict_lines():
    #         finished_offset = x + offset[0], y + offset[1]
    #         if finished_offset[0] > 0 and finished_offset[1] > 0:
    #             for line2 in new_grid[finished_offset].get_strict_lines():
    #                 if line1 == line2:
    #                     return True
    # return False
        # for line2 in thing2.get_strict_lines():
        #     if line1 == line2:
        #         return True
# print(new_grid)
# todo = list(sorted(new_grid.items(), key=lambda x: x[0][0]**x[0][1]))
last_pos = 0, 0
# for x,y in gen_xy_square_spiral(int(len(things)**.5)):

# for pos,block in todo:
#     for transform in block.get_transforms():
#         tmp_block = Block(block.id, transform)
#         if check_if_works(tmp_block, new_grid[last_pos]):
#             new_grid[pos] = tmp_block
#     last_pos = pos

for start_transform in new_grid[0,0].get_transforms():
    works = set()
    new_grid[0,0] = Block(new_grid[0,0].id, start_transform)
    for y in range(grid_size + 1):
        for transform in new_grid[0,y].get_transforms():
            tmp_block = Block(new_grid[0,y].id, transform)
            if y == 0 or check_if_works_up(tmp_block, new_grid[0, y-1]):
                new_grid[0,y] = tmp_block
                works.add(new_grid[0,y])
                break
        for x in range(1, grid_size + 1):
            for transform in new_grid[x,y].get_transforms():
                tmp_block = Block(new_grid[x,y].id, transform)
                if check_if_works_left(tmp_block, new_grid[x-1, y]):
                    works.add(new_grid[x,y])
                    new_grid[x,y] = tmp_block
                    break
    # print(len(works), len(new_grid))
    if len(works) == len(new_grid):
        break


def slice_per(source, step):
    return [source[i::step] for i in range(step)]




thing = []
thing2 = []
for x in range(grid_size + 1):
    thing2.append([])
    for y in range(grid_size + 1):
        thing2[x] += new_grid[x,y].get_grid_without_borders()
        thing = list(np.append(thing, new_grid[x,y].get_grid_without_borders()))

thing3 = []
for y,col in enumerate(thing2[:]):
    thing3.append([])
    for row in col:
        # print(y, row)
        thing3[y] += row

# pprint(thing3, compact=True)

thing = slice_per(thing, int(len(thing)**.5))

new_new_grid = defaultdict(str)

for y,line in enumerate(thing):
    for x,t in enumerate(line):
        new_new_grid[x,y] = "#" if t else "."

sorted_grid = dict(sorted(new_grid.items()))

for key,item in sorted_grid.items():
    print(item)

# print(Block(new_grid[1,0].id, new_grid[1,0].get_grid_without_borders()))

# print()

# print(new_grid)

# for pos,block in new_grid.items():
    

# def pprint_grid():
#     rangething = range(max(grid.keys(), key=lambda x: x[0]))
#     for y in rangething:
#         row = ""
#         for x in rangething:
#             print(grid[x,y])

# sea_monster = """
#                   # 
# #    ##    ##    ###
#  #  #  #  #  #  #   """

sea_monster_offsets = [
    (0,0),
    (1,1),
    (4,1),
    (5,0),
    (6,0),
    (7,1),
    (10,1),
    (11,0),
    (12,0),
    (13,1),
    (16,1),
    (17,0),
    (18,0),
    (19,0),
    (18,-1)
]

# new_sea_monster = []
# for y,line in enumerate(sea_monster.splitlines()):
hash_count = 0
#     new_sea_monster.append([])
#     for x,char in enumerate(line):
#         new_sea_monster[y].append(True if char == "#" else None)

def get_transforms(target):
        transforms = []

        for i in (0,1,2,3):
            rotated = rotate(target, i)
            transforms.append(flip(rotated, False, False))
            transforms.append(flip(rotated, True, False))
            transforms.append(flip(rotated, True, True))
            transforms.append(flip(rotated, False, True))
        return transforms

sea_monsters = 0
for transform in get_transforms(thing):
    hash_count = 0
    for y,line in enumerate(transform):
        for x,item in enumerate(line):
            hash_count += 1 if item else 0
            all_has = True
            for offset in sea_monster_offsets:
                try:
                    pos = transform[y+offset[1]][x+offset[0]]
                    if not pos:
                        all_has = False
                except IndexError:
                    all_has = False
            if all_has:
                sea_monsters += 1

print(sea_monsters)

# for i in data:
#     # for 

print(hash_count - (len(sea_monster_offsets) * sea_monsters))
# def all_works():
#     for x in range(grid_size):
#         for y in range(grid_size):
#             if not check_if_works(new_grid[x,y], x,y):
#                 return False
#     return True

# while not all_works():
#     for i in range(4):
#         for x in range(grid_size):
#             for y in range(grid_size):
#                 for transform in all_transforms(new_grid[x,y].grid):
#                     new_block = Block(new_grid[x,y].id, transform)
#                     # print(repr(new_block))
#                     print()
#                     if check_if_works(new_block, x,y):
#                         new_grid[x,y] = new_block
#                         print(str(new_grid[x,y]))
#                         break

# grid_without_borders = [[[] for __ in range(grid_size + 1)] for _ in range(grid_size + 1)]

grid_without_borders = dict()

for coord,item in new_grid.items():
    grid_without_borders[coord] = item.get_grid_without_borders()

# fullthing = []
# for y in range(grid_size):
#     thing = grid_without_borders[0,0]
#     for x in range(grid_size):
#         thing = np.append(thing, grid_without_borders[x,y], axis=1)
#     print(thing)
#     fullthing = np.append(fullthing, thing)

# print(fullthing)

# pprint(grid_without_borders)

done_grid = []

# thing = chain.from_iterable(grid_without_borders)
# thing2 = chain.from_iterable(thing)

# for block in grid_without_borders:
#     done_grid += block
#     # for item in block[::-1]:
        

# for column in rotate(grid_without_borders, 3):
#     for block in rotate(column, 3):
#         for line in rotate(block, 2):
#             for pos in line[::-1]:
#                 print("#" if pos else ".", end="")
#             print(" ", end="")
#         print()
    # print()
# pprint(list(thing2))
# pprint(grid_without_borders)
