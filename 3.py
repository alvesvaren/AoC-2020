from typing import Dict, Tuple
import aoc

data = aoc.get_input(3).splitlines()

course: Dict[Tuple[int, int], bool] = {}
length = len(data[0])
for y, line in enumerate(data):
    for x, char in enumerate(line):
        course[x, y] = char == "#"


def check_slope(dx: int, dy: int):
    count, x, y = 0, 0, 0
    while 1:
        try:
            x += dx
            y += dy
            if course[x % length, y]:
                count += 1
        except KeyError:
            break
    return count


val1 = check_slope(3, 1)
val2 = val1 * \
    check_slope(1, 1) * check_slope(5, 1) * \
    check_slope(7, 1) * check_slope(1, 2)

print("Part 1:", val1)
print("Part 2:", val2)
