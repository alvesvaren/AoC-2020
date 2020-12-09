import aoc

data = *map(int, aoc.get_input(9).splitlines()),

length = 25
for end in range(length, len(data)):
    to_sum = data[end]
    any_matches = False
    for num1 in data[end-length:end]:
        for num2 in data[end-length:end]:
            if num1+num2 == to_sum and num1 != num2:
                any_matches = True

    if not any_matches:
        print("Part 1:", to_sum)
        sum_to, starti, endi = 0, 0, 0
        largest_range = range(0)
        for starti in range(0, end):
            i = starti
            sum_to = 0
            while sum_to < to_sum and i < end:
                sum_to += data[i]
                i += 1
            if sum_to != to_sum:
                continue
            range_thing = range(starti, i-1)
            if len(range_thing) > len(largest_range):
                largest_range = range_thing
        data_range = data[largest_range.start:largest_range.stop]
        print("Part 2:", min(data_range) + max(data_range))
        break
