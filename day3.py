from util import read_lines_as_list


def calculate_trees_hit(right, down):
    input_data = read_lines_as_list('data/day3.txt')
    n = len(input_data[0])
    trees = 0
    horizontal_ptr = 0
    for row in input_data[down::down]:
        horizontal_ptr = (horizontal_ptr + right) % n
        if row[horizontal_ptr] == '#':
            trees += 1
    return trees

def part1():
    return calculate_trees_hit(3, 1)

def part2():
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    product = 1
    for right, down in slopes:
        product *= calculate_trees_hit(right, down)
    return product

if __name__ == '__main__':
    print(part1())
    print(part2())
