

def read_input() -> list:
    with open('./days/day6/input.txt', 'r') as file:
        return file.readline()


def find_marker() -> int:
    signal = read_input()
    chars = list(signal[:4])

    for i in range(4, len(signal)):
        if len(set(chars)) == 4:
            return i
        else:
            chars.pop(0)
        chars.append(signal[i])
    return 0


print(find_marker())
