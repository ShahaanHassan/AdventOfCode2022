def read_input() -> list:
    with open('./days/day4/input.txt', 'r') as file:
        return [line.rstrip().split(',') for line in file]


def find_overlaps() -> int:
    duties = read_input()
    score = 0
    for first, second in read_input():
        a,b = first.split('-')
        c,d = second.split('-')

        if set(range(int(a), int(b) + 1)).intersection(range(int(c), int(d) + 1)):
            score += 1
    return score


print(find_overlaps())