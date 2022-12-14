

def read_input() -> list:
    with open('./days/day8/input.txt', 'r') as file:
        return [[int(x) for x in line.rstrip()] for line in file]


def get_col(y, forrest) -> list:
    return [row[y] for row in forrest]


def all_smaller(tree, line) -> bool:
    for other_tree in line:
        if other_tree >= tree:
            return False
    return True


def check_tree(x, y, forrest) -> int:
    tree = forrest[x][y]
    if  all_smaller(tree, forrest[x][:y]) or all_smaller(tree, forrest[x][y+1:]) or \
         all_smaller(tree, get_col(y, forrest)[:x]) or \
            all_smaller(tree, get_col(y, forrest)[x+1:]):
        return 1
    else:
        return 0


def highest_trees():
    forrest = read_input()
    total = len(forrest)*4 - 4
    for x, row in enumerate(forrest[1:len(forrest) - 1], 1):
        for y in range(1, len(row) - 1):
            total += check_tree(x, y, forrest)
    return total


print(highest_trees())
