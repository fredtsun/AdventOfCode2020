from collections import Counter

from util import read_lines_as_list

class Password(object):
    def __init__(self, s):
        self._parse(s)

    def _parse(self, s):
        '''Some hacky parsing on a given input string. Use in __init__ only

        Example string: 9-11 p: pppppppppxblp
        1. splits by space first -> ['9-11'], p:, pppppppppxblp
        2. parses ['9-11'] and stores as `self.min` and `self.max`
        3. strips off the `:` in the given letter and stores in `self.letter`
        4. stores password as raw string and a freq map via collections.Counter
        '''
        *freq, letter, password = s.split(' ')
        assert len(freq) == 1, "Naughty list here we come"
        self.min, self.max = [int(n) for n in freq[0].split('-')]
        self.letter = letter[:-1]
        self.password = password
        self.password_freq = Counter(self.password)

    def is_valid(self):
        return self.min <= self.password_freq[self.letter] <= self.max

    def is_valid_part2(self):
        lower_idx = self.min - 1
        upper_idx = self.max - 1
        # EXACTLY one character in the given indices should match with the expected letter
        # so just xor the result of the comparisons
        return bool(self.password[lower_idx] == self.letter) ^ bool(self.password[upper_idx] == self.letter)


def part1():
    input_data = read_lines_as_list('data/day2.txt')
    passwords = [Password(s) for s in input_data]
    return len([pwd for pwd in passwords if pwd.is_valid()])


def part2():
    input_data = read_lines_as_list('data/day2.txt')
    passwords = [Password(s) for s in input_data]
    return len([pwd for pwd in passwords if pwd.is_valid_part2()])


if __name__ == '__main__':
    print(part1())
    print(part2())