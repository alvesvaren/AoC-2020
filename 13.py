import aoc
from sympy.ntheory.modular import crt
arrival, schedule = aoc.get_input(13).splitlines()

arrival = int(arrival)
busses = schedule.split(",")

minimum_bus = tuple()
for bus in busses:
    if bus == "x":
        continue
    bus = int(bus)

    first_arrival_from_bus_later_than_arrival_timestamp = max(range(bus, arrival+bus, bus))
    if not minimum_bus or first_arrival_from_bus_later_than_arrival_timestamp < minimum_bus[1]:
        minimum_bus = (bus, first_arrival_from_bus_later_than_arrival_timestamp)

# https://www.geeksforgeeks.org/python-sympy-crt-method/ heh
m = []
v = []
for i, bus in enumerate(busses):
    if bus != "x":
        bus = int(bus)
        m.append(bus)
        v.append(bus - i)

print("Part 1:", minimum_bus[0]*(minimum_bus[1]-arrival))
print("Part 2:", crt(m, v)[0])
