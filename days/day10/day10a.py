

def read_input() -> list:
    with open('./days/day10/input.txt', 'r') as file:
        return [tuple(line.strip().split(' ')) for line in file]


def check_cycle(cycle) -> bool:
    return cycle == 20 or (cycle - 20) % 40 == 0


def process_instructions() -> int:
    input = read_input()
    sum = cycle = 0
    register = 1
    for command in input:
        if command[0] == 'addx':
            for _ in range(2):
                cycle += 1
                if check_cycle(cycle):
                    sum += cycle * register
            register += int(command[1])
        else:
            cycle += 1
            if check_cycle(cycle):
                sum += cycle * register
    return sum


print(process_instructions())
