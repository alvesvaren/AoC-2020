import aoc,re

data = aoc.get_input(12).splitlines()

e,n,r = 0, 0, 0
we, wn = 1, 10
for instruction in data:
    direction, value = re.match(r"([NSFWELR])(\d+)", instruction).groups()
    value = int(value)
    
    if direction == "F":
        r = r % 4
        if r == 1:
            direction = "N"
        elif r == 2:
            direction = "W"
        elif r == 3:
            direction = "S"
        elif r == 0:
            direction = "E"
    if direction == "R":
        r -= value//90
    elif direction == "L":
        r += value//90
    elif direction == "N":
        e += value
    elif direction == "S":
        e -= value
    elif direction == "E":
        n += value
    elif direction == "W":
        n -= value
    
print(abs(e)+abs(n))