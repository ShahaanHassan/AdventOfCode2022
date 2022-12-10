from math import floor


def read_input() -> list:
    with open('./days/day10/input.txt', 'r') as file:
        return [tuple(line.strip().split(' ')) for line in file]


def add_pixel(cycle, register, output) -> bool:
    middle = register + (floor(cycle / 40) * 40)
    if cycle - 1 in [middle - 1, middle, middle + 1]:
        output.append('#')
    else:
        output.append('.')


def process_instructions() -> int:
    input = read_input()
    cycle = 0
    register = 1
    output = []
    for command in input:
        if command[0] == 'addx':
            for _ in range(2):
                cycle += 1
                add_pixel(cycle, register, output)
            register += int(command[1])
        else:
            cycle += 1
            add_pixel(cycle, register, output)
    return output


output = process_instructions()

for i, p in enumerate(output, 1):
    if i % 40 == 0:
        print()
    else:
        print(p, end='')
