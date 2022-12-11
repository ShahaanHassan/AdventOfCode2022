import re


class Monkey:

    def __init__(self, starting, operation, test, t_test, f_test):
        self.items = starting
        self.operation = operation
        self.test = test
        self.t_test = t_test
        self.f_test = f_test
        self.count = 0

    def do_operation(self, item) -> int:
        opr, val = self.operation
        val = item if val == 'old' else int(val)
        if opr == '*':
            return item * val
        else:
            return item + val

    def do_test(self, item) -> int:
        return self.t_test if item % self.test == 0 else self.f_test
    


def get_monkey_lines(file):
    for _ in range(5):
        yield file.readline().rstrip()
    file.readline()


def read_input() -> list:
    with open('./days/day11/input.txt', 'r') as file:
        monkeys = []
        while file.readline():
            monkey_lines = tuple(get_monkey_lines(file))
            starting = [int(x) for x in monkey_lines[0][18:].split(', ')]
            operation = monkey_lines[1][23:].split(' ')
            test = int(monkey_lines[2][20:])
            t_true = int(re.findall('\d+', monkey_lines[3])[0])
            f_true = int(re.findall('\d+', monkey_lines[4])[0])
            monkeys.append(Monkey(starting, operation, test, t_true, f_true))
        return monkeys


def monkey_inspection() -> int:
    monkeys = read_input()
    
    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                thrown_item = monkey.do_operation(item)
                thrown_item //= 3
                throw_to = monkey.do_test(thrown_item)
                monkeys[throw_to].items.append(thrown_item)
                monkey.count += 1
            monkey.items = []

    thrown_items = sorted(m.count for m in monkeys)
    return thrown_items[-1] * thrown_items[-2]

print(monkey_inspection())