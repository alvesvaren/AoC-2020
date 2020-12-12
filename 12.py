import aoc
import re

data = aoc.get_input(12).splitlines()

n, e, r = 0, 0, 0
e2, n2 = 0, 0
we, wn = 10, 1
for instruction in data:
    direction, value = re.match(r"([NSFWELR])(\d+)", instruction).groups()
    value = int(value)
    orig_direction = direction

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

        e2 += we * value
        n2 += wn * value

    if direction == "R":
        r -= value//90
    elif direction == "L":
        r += value//90
    elif direction == "N":
        n += value
    elif direction == "S":
        n -= value
    elif direction == "E":
        e += value
    elif direction == "W":
        e -= value

    if orig_direction == "R":
        if value == 90:
            we, wn = wn, -we
        elif value == 270:
            we, wn = -wn, we
        else:
            we, wn = -wn, -we
    elif orig_direction == "L":
        if value == 90:
            we, wn = wn, we
        elif value == 270:
            we, wn = wn, -we
        else:
            we, wn = -wn, -we
    elif orig_direction == "N":
        wn += value
    elif orig_direction == "S":
        wn -= value
    elif orig_direction == "E":
        we += value
    elif orig_direction == "W":
        we -= value
    # print(instruction, e, n, r)
    print(instruction, we, wn, e2, n2)

print(abs(e)+abs(n))
print(abs(e2)+abs(n2))
