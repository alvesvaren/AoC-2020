import aoc

data = map(int, aoc.get_input(1).splitlines())

def part1():
    for num1 in data:
        for num2 in data:
            if num1 + num2 == 2020:
                print(num1, num2)
                return num1 * num2

def part2():
    for num1 in data:
        for num2 in data:
            for num3 in data:
                if num1 + num2 + num3 == 2020:
                    print(num1, num2)
                    return num1 * num2 * num3

print(part1())
print(part2())
