from ast import literal_eval
from functools import cmp_to_key

def read_input() -> list:
    with open('./days/day13/input.txt', 'r') as file:
        return [list(convert_to_list(line.split('\n'))) for line in file.read().split('\n\n')]


def convert_to_list(pair: list) -> list:
    for li in pair:
        yield literal_eval(li)


def check_pairs():
    input = read_input()
    packets = []
    total = 0
    for i, pair in enumerate(input, 1):
        packets.append(pair[0])
        packets.append(pair[1])
        if right_order(pair[0], pair[1]) == 1:
            total += i
    a = sorted(packets + [[[2]]] + [[[6]]], key = cmp_to_key(right_order), reverse=True)
    return (a.index([[2]]) + 1) * (a.index([[6]]) + 1)
    

def right_order(first, second):    
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return 1
        elif first > second:
            return -1

    if isinstance(first, int) and isinstance(second, list):
        return right_order([first], second)

    if isinstance(first, list) and isinstance(second, int):
        return right_order(first, [second])

    if isinstance(first, list) and isinstance(second, list):
        for i in range(max(len(first), len(second))):
            if len(first) < i + 1:
                return 1
            if len(second) < i + 1:
                return -1
            order = right_order(first[i], second[i])
            if order is not None:
                return order


print(check_pairs())