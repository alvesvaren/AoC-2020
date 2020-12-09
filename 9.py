import aoc
from itertools import permutations

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
        print(to_sum)
        sum2, starti, endi = 0, 0, 0
        largest_range = []
        for starti in range(0, end):
            i = starti
            sum2 = 0
            while sum2 < to_sum and i < end:
                sum2 += data[i]
                print(i, sum2)
                
                i += 1
            if sum2 != to_sum:
                continue
            range_thing = range(starti, i-1)
            if len(range_thing)  > len(largest_range):
                largest_range = range_thing
        print(largest_range)
        data_range = data[largest_range.start:largest_range.stop]
        print(min(data_range) + max(data_range))
        break