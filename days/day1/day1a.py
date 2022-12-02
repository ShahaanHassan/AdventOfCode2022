
def read_input() -> list:
    with open('./days/day1/input.txt', 'r') as file:
        return file.read().split('\n\n')


def highest_calories(calories: list) -> int:
    return max([sum([int(y.rstrip()) for y in x.split('\n')]) for x in calories])


def highest_calories2(calories: list) -> int:
    a = sorted([sum([int(y.rstrip()) for y in x.split('\n')]) for x in calories], reverse=True)
    b = sum(a[:3])
    print()


print(highest_calories(read_input()))