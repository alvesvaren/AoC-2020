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
    while True:
        try:
            x += dx
            y += dy
            if course[x % length, y]:
                count += 1
        except KeyError:
            break
    return count


trees1 = check_slope(3, 1)
trees2 = trees1 * \
    check_slope(1, 1) * check_slope(5, 1) * \
    check_slope(7, 1) * check_slope(1, 2)

print("Part 1:", trees1)
print("Part 2:", trees2)
