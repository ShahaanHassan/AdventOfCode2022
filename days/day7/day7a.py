
from collections import deque

class Directory:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = {}
        self.children = {}

    def add_child(self, child):
        self.children[child.name] = child

    def add_file(self, size, filename):
        self.files[filename] = size
    
    def get_file_size(self) -> int:
        return sum(self.files.values()) + sum(dir.get_file_size() for dir in self.children.values())


def read_input() -> list:
    with open('./days/day7/input.txt', 'r') as file:
        return [line.rstrip() for line in file]


def get_file_tree():
    commands = read_input()
    root_directory = Directory('/')
    current_directory = root_directory

    for command in commands:
        if command.startswith('$'):
            if command[2:4] == 'cd':
                dest = command[5:]
                if dest == '..':
                    current_directory = current_directory.parent
                elif dest == '/':
                    current_directory = root_directory
                else:
                    current_directory = current_directory.children[dest]
        else:
            if command.startswith('dir'):
                dir_name = command[4:]
                current_directory.children[dir_name] = Directory(dir_name, current_directory)
            else:
                size, name = command.split(' ')
                current_directory.add_file(int(size), name)
    return root_directory


def get_big_ones(root_dir):
    sum = 0
    queue = deque([root_dir])
    while len(queue) != 0:
        current_dir = queue.pop()
        size = current_dir.get_file_size()
        if size <= 100000:
            sum += size
        queue += current_dir.children.values()
    return sum
        


print(get_big_ones(get_file_tree()))
