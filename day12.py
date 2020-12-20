from copy import deepcopy
from util import read_lines_as_list

NORTH = 'N'
SOUTH = 'S' 
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

left_direction_changes = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH
}

right_direction_changes = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

class Direction(object):
    def __init__(self, s):
        self.direction = s[0]
        self.movement = int(s[1:])

    def apply(self, curr_x, curr_y, facing):
        if self.direction in {NORTH, SOUTH, EAST, WEST}:
            curr_x, curr_y = self.directional_move(curr_x, curr_y, self.direction)
        elif self.direction == 'F':
            curr_x, curr_y = self.directional_move(curr_x, curr_y, facing)
        else:
            facing = self.adjust_direction(facing)
        return curr_x, curr_y, facing

    def adjust_direction(self, current_facing):
        change_map = left_direction_changes if self.direction == LEFT else right_direction_changes
        for _ in range(self.movement // 90):
            current_facing = change_map[current_facing]
        return current_facing

    def directional_move(self, curr_x, curr_y, facing):
        if facing == NORTH:
            curr_y += self.movement
        elif facing == SOUTH:
            curr_y -= self.movement        
        elif facing == EAST:
            curr_x += self.movement
        elif facing == WEST:
            curr_x -= self.movement
        else:
            raise Exception("Naughty list...")
        return curr_x, curr_y

def part1():
    directions = [Direction(s) for s in read_lines_as_list('data/day12.txt')]
    facing = EAST
    x, y = (0, 0)
    for d in directions:
        x, y, facing = d.apply(x, y, facing)
    return abs(x) + abs(y)

def part2():
    def convert_clockwise(direction):
        if d.direction == 'R':
            return direction.movement
        else:
            if direction.movement == 90:
                return 270
            elif direction.movement == 180:
                return 180
            else:
                return 90

    def turn_clockwise(waypoint, direction):
        degrees = convert_clockwise(direction)
        for _ in range(degrees // 90):
            wx, wy = waypoint
            waypoint = (wy, -wx)
        return waypoint
    
    directions = [Direction(s) for s in read_lines_as_list('data/day12.txt')]
    waypoint = (10, 1)
    ship_location = (0, 0)
    for d in directions:
        if d.direction == 'F':
            ship_x, ship_y = ship_location
            wp_x, wp_y = waypoint
            ship_location = (ship_x + d.movement * wp_x, ship_y + d.movement * wp_y)
        elif d.direction in {'L', 'R'}:
            waypoint = turn_clockwise(waypoint, d)
        else:
            wx, wy, _ = d.apply(waypoint[0], waypoint[1], d.direction)
            waypoint = (wx, wy)
    return abs(ship_location[0]) + abs(ship_location[1])

if __name__ == '__main__':
    print(part1())
    print(part2())