
def read_input() -> list:
    with open('./days/day3/input.txt', 'r') as file:
        return [line.rstrip() for line in file]


def get_score(c: str) -> int:
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38


def get_sum() -> int:
    score = 0
    for items in read_input():
        first_half, last_half = set(items[len(items) // 2:]), set(items[:len(items) // 2])
        common = first_half&last_half
        score += get_score(common.pop())
    return score

print(get_sum())