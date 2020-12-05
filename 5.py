import aoc

data = aoc.get_input(5).splitlines()
passes = []

for i, boarding_pass in enumerate(data):
    row, midworth, maxworth = 0, 0, 128
    seat, cmidworth, cmaxworth = 0, 0, 8
    bit = False
    for j, char in enumerate(boarding_pass):
        midworth, cmidworth = (row + maxworth)//2, (seat + cmaxworth)//2
        if char == "F":
            maxworth = midworth
        elif char == "B":
            row = midworth
        elif char == "L":
            cmaxworth = cmidworth
        else:
            seat = cmidworth
    
    passes.append(row*8 + seat)

last_value, answer2 = min(passes) - 1, 0
for row in sorted(passes):
    if last_value != row - 1:
        answer2 = last_value + 1
    last_value = row

print("Part 1:", max(passes))
print("Part 2:", answer2)