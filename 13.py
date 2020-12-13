import aoc
from sympy.ntheory.modular import crt

arrival, schedule = aoc.get_input(13).splitlines()
busses = schedule.split(",")
arrival = int(arrival)

minimum_bus = ()
for bus in busses:
    if bus == "x":
        continue
    bus = int(bus)

    first_bus_after_arrival = max(range(bus, arrival+bus, bus))
    if not minimum_bus or first_bus_after_arrival < minimum_bus[1]:
        minimum_bus = (bus, first_bus_after_arrival)

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
