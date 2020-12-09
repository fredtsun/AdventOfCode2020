from collections import Counter

from util import read_lines_as_list


def part1():
    input_data = read_lines_as_list('data/day9.txt')
    nums = [int(s) for s in input_data]
    counter = Counter(nums[:25])
    
    def can_find_sum(num):
        for k in counter.keys():
            comp = num - k
            if (comp == k and counter[comp] >= 2):
                    return True
            elif counter[comp] >= 1:
                return True
            else:
                pass
        return False

    for idx in range(25, len(nums)):
        num = nums[idx]
        if not can_find_sum(num):
            return num
        counter[num] += 1
        counter[nums[idx - 25]] -= 1
        if counter[nums[idx - 25]] == 0:
            del counter[nums[idx - 25]]

def part2():
    input_data = read_lines_as_list('data/day9.txt')
    nums = [int(s) for s in input_data]
    invalid_num = part1()
    s = 0
    left = 0
    right = 0
    while right < len(nums):
        s += nums[right]
        while s > invalid_num:
            s -= nums[left]
            left += 1
        right += 1
        if s == invalid_num:
            return min(nums[left:right]) + max(nums[left:right])
    raise Exception("U did this wrong")

if __name__ == '__main__':
    print(part1())
    print(part2())