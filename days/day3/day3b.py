
def read_input() -> list:
    with open('./days/day3/input.txt', 'r') as file:
        return [line.rstrip() for line in file]


def get_score(c: str) -> int:
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38


def get_sum() -> int:
    score = 0
    items = read_input();
    for i in range(0, len(items), 3):
        a, b, c = set(items[i]), set(items[i+1]), set(items[i+2])
        common = a & b & c
        score += get_score(common.pop())
    return score

print(get_sum())