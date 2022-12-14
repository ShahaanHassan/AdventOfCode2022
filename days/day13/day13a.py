from ast import literal_eval

def read_input() -> list:
    with open('./days/day13/input.txt', 'r') as file:
        return [list(convert_to_list(line.split('\n'))) for line in file.read().split('\n\n')]


def convert_to_list(pair: list) -> list:
    for li in pair:
        yield literal_eval(li)


def check_pairs():
    input = read_input()
    total = 0
    for i, pair in enumerate(input, 1):
        if right_order(pair[0], pair[1]) == 1:
            total += i
    return total
    

def right_order(first, second):    
    if isinstance(first, list) and isinstance(second, list):
        for i in range(max(len(first), len(second))):
            if len(first) < i+1:
                return 1
            if len(second) < i+1:
                return 0
            order = right_order(first[i], second[i])
            if order is not None:
                return order
    
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return 1
        elif first > second:
            return 0

    if isinstance(first, int) and isinstance(second, list):
        return right_order([first], second)

    if isinstance(first, list) and isinstance(second, int):
        return right_order(first, [second])


print(check_pairs())