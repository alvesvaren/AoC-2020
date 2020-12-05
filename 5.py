import aoc

data = aoc.get_input(5).splitlines()
passes = []

for boarding_pass in data:
    row, midrow, maxrow = 0, 0, 128
    seat, midseat, maxseat = 0, 0, 8
    for char in boarding_pass:
        midrow  = (row + maxrow)//2
        midseat = (seat + maxseat)//2
        if char == "F":
            maxrow = midrow
        elif char == "B":
            row = midrow
        elif char == "L":
            maxseat = midseat
        else:
            seat = midseat
    passes.append(row * 8 + seat)

last_value = min(passes) - 1
answer1, answer2 = max(passes), 0
for row in sorted(passes):
    if last_value != row - 1:
        answer2 = last_value + 1
    last_value = row

print("Part 1:", answer1)
print("Part 2:", answer2)
