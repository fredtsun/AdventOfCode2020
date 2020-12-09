from collections import defaultdict

from util import read_lines_as_list


class Instruction(object):
    def __init__(self, line):
        self.line = line

    def execute(self, acc, ptr):
        acc_change = 0
        ptr_change = 0
        if self.instruction_type == 'nop':
            ptr_change = 1
        elif self.instruction_type == 'jmp':
            ptr_change = int(self.line.lstrip('jmp '))
        elif self.instruction_type == 'acc':
            acc_change = int(self.line.lstrip('acc '))
            ptr_change = 1
        else:
            raise Exception("Naughty list!!!")
        return acc + acc_change, ptr + ptr_change
    
    def change_and_execute(self, acc, ptr):
        old_line = str(self.line)
        if self.instruction_type == 'jmp':
            self.line = self.line.replace('jmp', 'nop')
        elif self.instruction_type == 'nop':
            self.line = self.line.replace('nop', 'jmp')
        else:
            raise Exception("YOU ARE NAUGHTY!")
        new_acc, new_ptr = self.execute(acc, ptr)
        self.line = old_line
        return new_acc, new_ptr
    
    @property
    def instruction_type(self):
        if self.line.startswith('nop'):
            return 'nop'
        elif self.line.startswith('jmp'):
            return 'jmp'
        elif self.line.startswith('acc'):
            return 'acc'
        else:
            raise Exception("WTF IS THIS?")

def part1():
    input_data = read_lines_as_list('data/day8.txt')
    instructions = [Instruction(data) for data in input_data]
    lines_executed = set()
    acc = 0
    ptr = 0
    while ptr not in lines_executed:
        lines_executed.add(ptr)
        acc, ptr = instructions[ptr].execute(acc, ptr)
    return acc

def find_broken_lines(instructions):
    lines_executed = defaultdict(int)
    acc = 0
    ptr = 0
    while lines_executed[ptr] < 3:
        lines_executed[ptr] += 1
        acc, ptr = instructions[ptr].execute(acc, ptr)
    # only allowed to switch from jump -> acc or acc -> jump
    return [idx for idx in list(lines_executed.keys()) if instructions[idx].instruction_type != 'acc']

def fix_program_and_get_acc(instructions, fix_line):
    lines_executed = set()
    acc = 0
    ptr = 0
    while ptr not in lines_executed and ptr < len(instructions):
        lines_executed.add(ptr)
        instruction = instructions[ptr]
        if ptr == fix_line:
            acc, ptr = instruction.change_and_execute(acc, ptr)
        else:
            acc, ptr = instruction.execute(acc, ptr)
    return acc if ptr == len(instructions) else None

def part2():
    input_data = read_lines_as_list('data/day8.txt')
    instructions = [Instruction(data) for data in input_data]
    broken_lines = find_broken_lines(instructions)
    fix_attempts = [fix_program_and_get_acc(instructions, bl) for bl in broken_lines]
    answer = [fa for fa in fix_attempts if fa is not None]
    assert len(answer) == 1, "you did this problem wrong dude"
    return answer[0]

if __name__ == '__main__':
    print(part1())
    print(part2())