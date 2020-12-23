import aoc
from collections import deque

data = [int(i) for i in aoc.get_input(23).strip()]

pos = 0
for move in range(100):
    to_slice = slice(pos+1, pos+4)
    popped_cups = data[to_slice]
    destination = data[pos] - 1
    print(pos, data, popped_cups, end=" ")
    del data[to_slice]
    while destination not in data:
        destination -= 1
        if destination < min(data):
            destination = max(data)
    print(destination)
    destination = data.index(destination)

    pos += 1
    pos %= len(data)
    
    
    for i,element in enumerate(popped_cups,1):
        data.insert(destination + i, element)
    
    if destination < pos:
        for _ in range(3):
            data.append(data.pop(0))

print("".join(map(str,data[data.index(1)+1:] + data[:data.index(1)])))