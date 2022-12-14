

def read_input() -> list:
    with open('./days/day6/input.txt', 'r') as file:
        return file.readline()


def find_marker() -> int:
    signal = read_input()
    chars = list(signal[:14])

    for i in range(14, len(signal)):
        if len(set(chars)) == 14:
            return i
        else:
            chars.pop(0)
        chars.append(signal[i])
    return -1


print(find_marker())
