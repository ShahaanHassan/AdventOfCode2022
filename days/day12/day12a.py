from collections import deque
from math import inf


def read_input() -> list:
    with open('./days/day12/input.txt', 'r') as file:
        return [[c for c in line.strip()] for line in file]


def get_elevation(letter) -> int:
    if letter == 'S':
        return 1
    elif letter == 'E':
        return 26
    else:
        return ord(letter) - 96


def get_start(grid) -> tuple:
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == 'S':
                return (x, y)


def get_neighbours(point, grid):
    if point[0] > 0:
        yield (point[0] - 1, point[1])
    if point[0] < len(grid) - 1:
        yield (point[0] + 1, point[1])
    if point[1] > 0:
        yield (point[0], point[1] - 1)
    if point[1] + 1 < len(grid[0]) - 1:
        yield (point[0], point[1] + 1)


def get_shortest_path() -> int:
    grid = read_input()
    start = get_start(grid)
    queue = deque([start])
    seen = set()
    distances = {start: 0}

    while queue:
        current = queue.popleft()

        if current not in seen:
            if grid[current[0]][current[1]] == 'E':
                return distances[current]

            seen.add(current)
            for point in get_neighbours(current, grid):
                if point not in seen:
                    diff = get_elevation(grid[point[0]][point[1]]) - get_elevation(grid[current[0]][current[1]])
                    if diff <= 1:
                        queue.append(point)
                        distances[point] = distances[current] + 1
    return -1


print(get_shortest_path())
