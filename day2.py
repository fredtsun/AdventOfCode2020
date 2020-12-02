'''
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
'''
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