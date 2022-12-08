

def read_input() -> list:
    with open('./days/day8/input.txt', 'r') as file:
        return [[int(x) for x in line.rstrip()] for line in file]


def get_col(y, forrest) -> list:
    return [row[y] for row in forrest]


def get_view(tree, line) -> int:
    smaller = 0
    if not line:
        return smaller
    for other_tree in line:
        smaller += 1
        if other_tree >= tree:
            break
    return smaller


def check_tree_view(x, y, forrest) -> int:
    tree = forrest[x][y]
    total = get_view(tree, forrest[x][:y][::-1])
    total *= get_view(tree, forrest[x][y+1:])
    total *= get_view(tree, get_col(y, forrest)[:x][::-1])
    total *= get_view(tree, get_col(y, forrest)[x+1:])
    return total


def get_best_view():
    forrest = read_input()
    best_view = 0
    for x, row in enumerate(forrest[1:len(forrest) - 1], 1):
        for y in range(1, len(row) - 1):
            view = check_tree_view(x, y, forrest)
            if view > best_view:
                best_view = view
    return best_view


print(get_best_view())
