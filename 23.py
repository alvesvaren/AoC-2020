from typing import Iterable
import aoc

# https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)
class LinkedList:
    def __init__(self, startdata: Iterable) -> None:
        self.first = None
        self.head = None
        for i in startdata:
            node = self.push(i)
            if not self.first:
                self.first = node
    
    def push(self, data):
        node = Node(data, self.head)
        self.head = node
        return node
    
    def find(self, value):
        current = self.head

        while current != None:
            if current.data == value:
                return current
            current = current.next

    def __iter__(self):
        current = self.head
        while current != None:
            yield current
            current = current.next



data = [int(i) for i in aoc.get_input(23).strip()]
data_new_range = range(max(data)+1, 1000000+1)
full_data_range = range(1, data_new_range.stop)
min_val = min(data)
max_val = max(data_new_range)
data += list(data_new_range)
print("Creating linked list")
data = LinkedList(data)
lookup = {i.data: i for i in iter(data)}

# data.first.next = data.head

# pos = 0
# data.head = data.first
for move in range(10000000):
    if move % 100000 == 0:
        print(move)
        # print(list(lookup.items())[1:1000])
    # to_slice = slice(pos+1, pos+4)
    data_iter = iter(data)
    # try:
    popped_cups = (next(data_iter), next(data_iter), next(data_iter))#[::-1] # data[to_slice]
    # except StopIteration:
    #     continue
    # print(popped_cups)
    data.head.next = popped_cups[-1].next
    destination: int = data.head.data - 1
    if destination < 1:
            destination = full_data_range.stop-1
    while destination not in full_data_range or any(node.data == destination for node in popped_cups):
        destination -= 1
        if destination < 1:
            destination = full_data_range.stop-1
    # print(destination)
    destination_node = lookup[destination]
    popped_cups[-1].next = destination_node.next
    destination_node.next = popped_cups[0]
    data.head = data.head.next

    # pos += 1
    # pos %= len(data)
    
    
    # for i,element in enumerate(popped_cups,1):
    #     data.insert(destination + i, element)
    
    # if destination < pos:
    #     # data = data[3:] + data[:3]
    #     data.rotate(3)
    #     # for _ in range(3):
    #     #     data.append(data.pop(0))
# first_in_lookup: Node = lookup[0]
# found = data.find(1)
# lookup = {i.data: i for i in iter(data)}
# data.first.next = None
# lookup = {i.data: i for i in iter(data)}
# lookup[1] = data.find(1)
print(lookup[1].next.data * lookup[1].next.next.data)

## This version doesn't work, but had a "brute-force" version that ran for 35 minutes but was faster than finishing this