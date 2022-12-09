

def read_input() -> list:
    with open('./days/day9/input.txt', 'r') as file:
        return [tuple(line.strip().split(' ')) for line in file]


def move_ropey_snake() -> int:
    inputs = read_input()
    rope = [[0, 0] for _ in range(10)]
    visited = set([(0, 0)])
    for dir, dist in inputs:
        head = rope[0]
        for _ in range(int(dist)):
            if dir == 'R':
                head[1] += 1
            elif dir == 'L':
                head[1] -= 1
            elif dir == 'U':
                head[0] += 1
            elif dir == 'D':
                head[0] -= 1
            
            for i, knot in enumerate(rope[1:], 1):
                last_knot = rope[i - 1]
                x_diff, y_diff = abs(last_knot[0] - knot[0]), abs(last_knot[1] - knot[1])
                if x_diff > 1 or y_diff > 1:
                    if last_knot[0] < knot[0]:
                        knot[0] -= 1
                    elif last_knot[0] > knot[0]:
                        knot[0] += 1
                    
                    if last_knot[1] < knot[1]:
                        knot[1] -= 1
                    elif last_knot[1] > knot[1]:
                        knot[1] += 1
            visited.add((rope[-1][0], rope[-1][1]))
    return len(visited)

print(move_ropey_snake())