
def read_input() -> list:
    opponent, me = [], []
    with open('./days/day2/input.txt', 'r') as file:
        for line in file.readlines():
            a, b = line.split()
            opponent.append(a)
            me.append(b)
    return opponent, me


def get_move(o: str, outcome: int) -> int:
    losing_moves = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    winning_moves = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    if (outcome == 'w'):
        return ord(winning_moves.get(o)) - 87
    elif(outcome == 'l'):
        return ord(losing_moves.get(o)) - 87
    else:
        return ord(o) - 64


def get_score(o: str, m: str) -> int:
    if (m == 'X'):
        return get_move(o, 'l')
    elif (m == 'Y'):
        return 3 + get_move(o, 'd')
    else:
        return 6 + get_move(o, 'w')


def calculate_final_score() -> int:
    opponent, me = read_input()
    return sum(get_score(o, m) for o, m in zip(opponent, me))

print(calculate_final_score())