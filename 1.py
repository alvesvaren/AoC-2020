import aoc

data = {*map(int, aoc.get_input(1).splitlines())}

def part1():
    for num1 in data:
        for num2 in data:
            if num1 + num2 == 2020:
                return num1 * num2

def part2():
    for num1 in data:
        for num2 in data:
            for num3 in data:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

print("Part 1:", part1())
print("Part 2:", part2())
