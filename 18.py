import aoc
import re

data = aoc.get_input(18).splitlines()


def find_parenthese(expression: str, start: int):
    depth = 0
    for i, char in enumerate(expression):
        if i < start:
            continue
        if char == "(":
            depth += 1
        if char == ")":
            depth -= 1
            if depth == 0:
                return i
    raise IndexError


def calc(expression: str, depth: int):
    expression = expression.replace(" ", "")
    value = 0
    multiplication = False
    last_was_num = False
    next_index = 0
    num = ""
    for i, char in enumerate(expression + " "):
        if i < next_index:
            continue

        if char in map(str, range(0, 10)):
            num += char
            last_was_num = True
        else:
            if last_was_num:
                thing = int(num)
                if multiplication:
                    value *= thing
                else:
                    value += thing
                num = ""
                last_was_num = False
        if char == "(":
            next_index = find_parenthese(expression, i)
            if multiplication:
                value *= calc(expression[i+1:next_index], depth+1)
            else:
                value += calc(expression[i+1:next_index], depth+1)
        if char == "*":
            multiplication = True
        if char == "+":
            multiplication = False
    return value


sum1, sum2 = 0, 0
for line in data:
    sum1 += calc(line, 0)

print("Part 1:", sum1)
print("Part 2:", sum2)
