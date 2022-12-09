

def read_input() -> list:
    with open('./days/day9/input.txt', 'r') as file:
        return [tuple(line.strip().split(' ')) for line in file]


def move_ropey_snake() -> int:
    inputs = read_input()
    head, tail = [0, 0], [0, 0]
    visited = set([(0, 0)])
    for dir, dist in inputs:
        for _ in range(int(dist)):
            if dir == 'R':
                head[1] += 1
            elif dir == 'L':
                head[1] -= 1
            elif dir == 'U':
                head[0] += 1
            elif dir == 'D':
                head[0] -= 1
            
            x_diff, y_diff = abs(head[0] - tail[0]), abs(head[1] - tail[1])
            if x_diff > 1 or y_diff > 1:
                if head[0] < tail[0]:
                    tail[0] -= 1
                elif head[0] > tail[0]:
                    tail[0] += 1
                
                if head[1] < tail[1]:
                    tail[1] -= 1
                elif head[1] > tail[1]:
                    tail[1] += 1
            visited.add((tail[0], tail[1]))
    return len(visited)

print(move_ropey_snake())