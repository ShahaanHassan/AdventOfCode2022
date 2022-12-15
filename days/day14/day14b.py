from math import inf

def read_input() -> list:
    with open('./days/day14/input.txt', 'r') as file:
        return [[tuple(int(x) for x in reversed(point.split(','))) for point in line.rstrip().split(' -> ')] for line in file]


def draw_lines(points, grid, lowest):
    start = points.pop(0)
    while points:
        end = points.pop(0)
        if start[0] == end[0]:
            s, e = min(start[1], end[1]), max(start[1], end[1])
            for i in range(s - lowest, e - lowest + 1):
                grid[start[0]][i] = '#'
        else:
            s, e = min(start[0], end[0]), max(start[0], end[0])
            for i in range(s, e):
                grid[i][start[1] - lowest] = '#'
        start = end


def sand_is_falling_oh_no():
    input_lines = read_input()
    lowest_y = min(point[1] for line in input_lines for point in line) - 800
    highest_y = max(point[1] for line in input_lines for point in line) + 800
    highest_x = max(point[0] for line in input_lines for point in line)
    grid = [['.' for _ in range(5000)] for _ in range(3 + highest_x)]

    for points in input_lines:
        draw_lines(points, grid, lowest_y)
    grid[-1] = ['#' for _ in range(5000)]
    
    sand_in_void = False
    count = 0
    while True:
        # print_grid(grid)
        new_positions = []
        pos = [0,500-lowest_y]
        rested = False
        while not rested:
            new_x = pos[0] + 1
            if grid[0][500-lowest_y] == '#':
                return count
            if grid[new_x][pos[1] - 1:pos[1]+2] == ['#']*3:
                rested = True
                grid[pos[0]][pos[1]] = '#'
            else:
                pos[0] = new_x
                if grid[pos[0]][pos[1]] == '#':
                    if grid[pos[0]][pos[1] - 1] != '#':
                            pos[1] -= 1
                    else:
                        pos[1] += 1
        new_positions.append(pos)
        count += 1


print(sand_is_falling_oh_no())