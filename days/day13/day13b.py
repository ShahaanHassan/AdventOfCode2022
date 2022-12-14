from ast import literal_eval
from functools import cmp_to_key

def read_input() -> list:
    with open('./days/day13/input.txt', 'r') as file:
        return [x for line in file for x in convert_to_list(line.rstrip().split()) if line != '\n']


def convert_to_list(pair: list) -> list:
    for li in pair:
        yield literal_eval(li)


def check_pairs() -> int:
    input = read_input() + [[[2]], [[6]]]
    ordered = sorted(input, key=cmp_to_key(right_order), reverse=True)
    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)
    

def right_order(first, second) -> int: 
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
            if len(first) <= i:
                return 1
            if len(second) <= i:
                return -1
            order = right_order(first[i], second[i])
            if order is not None:
                return order



print(check_pairs())