from util import read_lines_as_list

def part1():
    input_data = read_lines_as_list('data/day1.txt')
    num_set = set([int(n) for n in input_data])
    for n in num_set:
        if 2020 - n in num_set:
            return n * (2020 - n)
    raise Exception("Looks like I'm on the naughty list :x")

def part2():
    input_data = read_lines_as_list('data/day1.txt')
    nums = [int(n) for n in input_data]
    complements = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            comp = 2020 - nums[i] - nums[j]
            if comp >= 0:
                complements[comp] = (i, j)
    
    for idx, num in enumerate(nums):
        if num not in complements:
            continue
        idx1, idx2 = complements[num]
        if idx != idx1 and idx != idx2:
            return nums[idx1] * nums[idx2] * num
    raise Exception("On the naughty list twice..")

if __name__ == '__main__':
    print(part1())
    print(part2())