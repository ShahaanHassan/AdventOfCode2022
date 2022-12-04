def read_input() -> list:
    with open('./days/day4/input.txt', 'r') as file:
        return [line.rstrip().split(',') for line in file]


def find_overlaps() -> int:
    duties = read_input()
    score = 0
    for first, second in read_input():
        a,b = first.split('-')
        c,d = second.split('-')

        if (((int(a) >= int(c)) and (int(b) <= int(d))) or ((int(a) <= int(c)) and (int(b) >= int(d)))):
            score += 1
    return score


print(find_overlaps())