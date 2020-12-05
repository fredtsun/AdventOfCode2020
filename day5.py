from util import read_lines_as_list

def binary_search(s, low, high, low_symb, high_symb):
    for c in s:
        middle = low + (high - low) // 2
        if c == low_symb:
            high = middle
        else:
            low = middle + 1
    assert low == high
    return low

def get_seat_id(s):
    row = binary_search(s[:7], 0, 127, 'F', 'B')
    seat = binary_search(s[7:], 0, 7, 'L', 'R')
    return row * 8 + seat

def part1():
    input_data = read_lines_as_list('data/day5.txt')
    return max([get_seat_id(data) for data in input_data])

def part2():
    input_data = read_lines_as_list('data/day5.txt')
    seat_ids = [get_seat_id(data) for data in input_data]
    return set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)

if __name__ == '__main__':
    print(part1())
    print(part2())
