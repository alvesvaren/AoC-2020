import aoc
import sys
from functools import lru_cache

arrival, schedule = aoc.get_input(13).splitlines()

arrival = int(arrival)
busses = schedule.split(",")

minimum_bus = tuple()
for bus in busses:
    if bus == "x":
        continue
    bus = int(bus)

    thing = max(range(bus, arrival+bus, bus))
    if not minimum_bus or thing < minimum_bus[1]:
        minimum_bus = (bus, thing)


print(minimum_bus[0]*(minimum_bus[1]-arrival))
