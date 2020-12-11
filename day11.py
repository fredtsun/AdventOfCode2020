from copy import deepcopy
from util import read_lines_as_list

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'
INPUT_DATA = [list(row) for row in read_lines_as_list('data/day11.txt')]
in_bounds = lambda x, y: 0 <= x < len(INPUT_DATA) and 0 <= y < len(INPUT_DATA[0])

def simulate_round(seats, find_occupied_seat_fn, adjacent_seats_to_free):
    new_seats = deepcopy(seats)

    def get_symbol(x, y):
        current_state = seats[x][y]
        if current_state == FLOOR:
            return FLOOR

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if current_state == EMPTY:
            for dx, dy in directions:
                if in_bounds(x + dx, y + dy) and find_occupied_seat_fn(x, dx, y, dy, seats):
                    return EMPTY
            return OCCUPIED
        
        else: # current_state == OCCUPIED
            count = 0
            for dx, dy in directions:
                if in_bounds(x + dx, y + dy) and find_occupied_seat_fn(x, dx, y, dy, seats):
                    count += 1
            return EMPTY if count >= adjacent_seats_to_free else OCCUPIED

    for i in range(len(seats)):
        for j in range(len(seats[0])):
            new_seats[i][j] = get_symbol(i, j)
    return new_seats


def simulate_all(find_occupied_seat_fn, adjacent_seats_to_free):
    current_seats = INPUT_DATA
    while True:
        new_seats = simulate_round(current_seats, find_occupied_seat_fn, adjacent_seats_to_free)
        if new_seats == current_seats:
            break
        current_seats = new_seats
    return current_seats


def part1():
    def occupied_rule(x, dx, y, dy, seats):
        return seats[x + dx][y + dy] == OCCUPIED

    seats = simulate_all(occupied_rule, 4)
    return len([seat for row in seats for seat in row if seat == OCCUPIED])


def part2():
    def occupied_rule(x, dx, y, dy, seats):
        while in_bounds(x + dx, y + dy):
            if seats[x + dx][y + dy] == FLOOR:
                x += dx
                y += dy
            else:
                return seats[x + dx][y + dy] == OCCUPIED
        return False
    seats = simulate_all(occupied_rule, 5)
    return len([seat for row in seats for seat in row if seat == OCCUPIED])

if __name__ == '__main__':
    print(part1())
    print(part2())