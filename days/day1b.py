
def read_input() -> list:
    with open('./days/input.txt', 'r') as file:
        return file.read().split('\n\n')


def highest_calories(calories: list) -> int:
    return sum(sorted([sum([int(y.rstrip()) for y in x.split('\n')]) for x in calories], reverse=True)[:3])


print(highest_calories(read_input()))