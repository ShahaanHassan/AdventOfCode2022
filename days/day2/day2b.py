
def read_input() -> list:
    opponent, me = [], []
    with open('./days/day2/input.txt', 'r') as file:
        for line in file.readlines():
            a, b = line.split()
            opponent.append(a)
            me.append(b)
    return opponent, me


def get_move(op, outcome):
    losing_moves = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    winning_moves = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    if (outcome == 'w'):
        return ord(winning_moves.get(op)) - 87
    elif(outcome == 'l'):
        return ord(losing_moves.get(op)) - 87
    else:
        return ord(op) - 64


def get_score(m, op):
    score = 0

    if (m == 'X'):
        score += get_move(op, 'l')
    elif (m == 'Y'):
        score += 3 + get_move(op, 'd')
    else:
        score += 6 + get_move(op, 'w')

    return score


def calculate_final_score():
    opponent, me = read_input()
    final_score = 0
    for o, m in zip(opponent, me):
        final_score += get_score(m, o)

    return final_score

print(calculate_final_score())