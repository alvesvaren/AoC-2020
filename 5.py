import aoc

data = aoc.get_input(5).splitlines()
passes = []

for boarding_pass in enumerate(data):
    row, midrow, maxrow = 0, 0, 128
    seat, midseat, maxseat = 0, 0, 8
    for char in boarding_pass:
        midrow, midseat = (row + maxrow)//2, (seat + maxseat)//2
        if char == "F":
            maxrow = midrow
        elif char == "B":
            row = midrow
        elif char == "L":
            maxseat = midseat
        else:
            seat = midseat
    
    passes.append(row*8 + seat)

last_value, answer2 = min(passes) - 1, 0
for row in sorted(passes):
    if last_value != row - 1:
        answer2 = last_value + 1
    last_value = row

print("Part 1:", max(passes))
print("Part 2:", answer2)