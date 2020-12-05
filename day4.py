from string_validation import (All, CustomRule, Enum, Exists, Length, Number,
                               ObjectRule, Switch)
from util import read_lines_as_list


def string_to_dict(s):
    # hack that will put me on the naughty list
    raw_data = ' '.join(s.split('\n')).split(' ')
    parsed = {}
    for data in raw_data:
        field, value = data.split(':')
        parsed[field] = value
    return parsed

SchemaPartOne = ObjectRule({
    'byr': Exists(), 
    'iyr': Exists(),
    'eyr': Exists(),
    'hgt': Exists(),
    'hcl': Exists(),
    'ecl': Exists(),
    'pid': Exists()
})

def hair_color_rule(value):
    alpha_set = set('abcdef')
    return (
        value[0] == '#' and 
        all(c.isdigit() or c in alpha_set for c in value[1:]))

SchemaPartTwo = ObjectRule({
    'byr': Number(len=4, min=1920, max=2003), 
    'iyr': Number(len=4, min=2010, max=2021),
    'eyr': Number(len=4, min=2020, max=2031),
    'hgt': Switch(
        eval_fn=lambda val: val[-2:],
        switch_config={
            'cm': lambda val: 150 <= int(val[:-2]) <= 193,
            'in': lambda val: 59 <= int(val[:-2]) <= 76
        }),
    'hcl': All(Length(7), CustomRule(hair_color_rule)),
    'ecl': Enum(values={'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}),
    'pid': All(Length(9), Number())
})

def part1():
    input_data = read_lines_as_list('data/day4.txt', split_pattern='\n\n')
    parsed = [string_to_dict(s) for s in input_data]
    return len([p for p in parsed if SchemaPartOne(p)])

def part2():
    input_data = read_lines_as_list('data/day4.txt', split_pattern='\n\n')
    parsed = [string_to_dict(s) for s in input_data]
    return len([p for p in parsed if SchemaPartTwo(p)])

if __name__ == '__main__':
    print(part1())
    print(part2())
