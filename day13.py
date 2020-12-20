from util import read_lines_as_list

def find_closest(bus_stop, earliest):
    mul = 1
    while True:
        time = mul * bus_stop
        if time < earliest:
            mul += 1
        else:
            return abs(time - earliest)

def part1():
    earliest, buses = read_lines_as_list('data/day13.txt')
    earliest = int(earliest)
    buses = [int(b) for b in buses.split(',') if b != 'x']
    closest_buses = sorted([(find_closest(b, earliest), b) for b in buses], key=lambda t: t[0])
    dist, bus_stop = closest_buses[0]
    return dist * bus_stop

def find_min_earliest(buses):
    max_bus_stop = max(b[1] for b in buses)
    first = buses[0][1]
    return max_bus_stop + (first - max_bus_stop % first)

def fits_condition(time, offset, bus_stop):
    return time % bus_stop == bus_stop - offset

def part2():
    _, buses = read_lines_as_list('data/day13.txt')
    buses = [(idx, int(b)) for idx, b in enumerate(buses.split(',')) if b != 'x']
    earliest = find_min_earliest(buses)
    first = buses[0][1]
    while True:
        print(ea)
        if any(not fits_condition(earliest, offset, bus_stop) for offset, bus_stop in buses[1:]):
            earliest += first
        else:
            return earliest

if __name__ == '__main__':
    # print(part1())
    print(part2())