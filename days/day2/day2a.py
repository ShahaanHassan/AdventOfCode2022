
def read_input() -> list:
    opponent, me = [], []
    with open('./days/day2/input.txt', 'r') as file:
        for line in file.readlines():
            a, b = line.split()
            opponent.append(a)
            me.append(b)
    return opponent, me


def get_outcome(opponent, me):
    moves = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    if (moves.get(opponent) == me):
        return 0
    elif (abs(ord(opponent) - ord(me)) == 23):
        return 3
    else:
        return 6


def get_score(shape, outcome):
    score = outcome
    if (shape == 'X'):
        score += 1
    elif (shape == 'Y'):
        score += 2
    else:
        score += 3

    return score


def calculate_final_score():
    opponent, me = read_input()
    final_score = 0
    for o, m in zip(opponent, me):
        final_score += get_score(m, get_outcome(o, m))

    return final_score

print(calculate_final_score())