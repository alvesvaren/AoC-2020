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

    thing = max(range(bus, arrival+bus, bus))
    if not minimum_bus or thing < minimum_bus[1]:
        minimum_bus = (bus, thing)

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
