import aoc,re

data = aoc.get_input(12).splitlines()

x,y,r = 0, 0, 0

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
        x += value
    elif direction == "S":
        x -= value
    elif direction == "E":
        y += value
    elif direction == "W":
        y -= value
    
print(abs(x)+abs(y))