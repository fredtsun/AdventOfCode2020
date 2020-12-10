from functools import lru_cache
from util import read_lines_as_list

def part1():
    input_data = read_lines_as_list('data/day10.txt')
    nums = sorted([int(n) for n in input_data])
    one_volt_diff = 0
    three_volt_diff = 0
    for prev, next_ in zip(nums[:-1], nums[1:]):
        if next_ - prev == 3:
            three_volt_diff += 1
        elif next_ - prev == 1:
            one_volt_diff += 1
        else:
            raise Exception("this broken")
    return (one_volt_diff + 1) * (three_volt_diff + 1)


def part2():
    input_data = read_lines_as_list('data/day10.txt')
    nums_set = set([int(n) for n in input_data])
    term = max(nums_set)

    @lru_cache
    def find_combinations(start):
        if start == term:
            return 1
        count = 0
        for i in range(1, 4):
            if start + i not in nums_set:
                continue
            count += find_combinations(start + i)
        return count
    return find_combinations(0)


if __name__ == '__main__':
    print(part1())
    print(part2())
