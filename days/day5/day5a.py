from collections import deque 
import re


def read_input() -> list:
    with open('./days/day5/input.txt', 'r') as file:
        stacks = []
        instructions = []
        for line in file:
            if line != '\n' and not line.startswith(' 1'):
                if not line.startswith('move'):
                    potential_crates = line[1::4]
                    for i, crate in enumerate(potential_crates):
                        if not stacks:
                            stacks = [deque() for x in range(len(potential_crates))]
                        if crate != ' ':
                            stacks[i].appendleft(crate)
                else:
                    instructions += [map(lambda x: int(x), re.findall('\d+', line))]
        return stacks, instructions


def stack_boxes() -> str:
    stacks, instructions = read_input()
    for instruction in instructions:
        amount, begin, end = instruction
        for _ in range(amount):
            stacks[end - 1].append(stacks[begin - 1].pop())
    return ''.join(s.pop() for s in stacks)


print(stack_boxes())