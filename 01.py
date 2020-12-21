import aoc

data = {*map(int, aoc.get_input(1).splitlines())}

val1, val2 = 0, 0
for num1 in data:
    if not (val1 and val2):
        for num2 in data:
            if not val2:
                for num3 in data:
                    if num1 + num2 + num3 == 2020:
                        val2 = num1 * num2 * num3
            if num1 + num2 == 2020:
                val1 = num1 * num2

print("Part 1:", val1)
print("Part 2:", val2)
