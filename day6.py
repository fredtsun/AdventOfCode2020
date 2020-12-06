from functools import reduce
from util import read_lines_as_list

def part1():
    input_data = read_lines_as_list('data/day6.txt', split_pattern='\n\n')
    group = [''.join(d.split('\n')) for d in input_data]
    return reduce(lambda acc, curr: acc + len(set(curr)), group, 0)

def group_consensus(s):
    group = set([chr(ord('a') + i) for i in range(0, 26)])
    for person_votes in s.split('\n'):
        group = group.intersection(set(person_votes))
    return len(group)

def part2():
    input_data = read_lines_as_list('data/day6.txt', split_pattern='\n\n')
    return reduce(lambda acc, curr: acc + group_consensus(curr), input_data, 0)

if __name__ == '__main__':
    print(part1())
    print(part2())
