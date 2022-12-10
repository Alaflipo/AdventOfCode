def write_directories(current_directory, instructions):
    while len(instructions) > 0:
        instruction = instructions.pop(0).strip().split(' ')
        if (instruction[0] == '$'):
            if (instruction[1] == 'cd'):
                directory = instruction[2]
                if (directory == '..'):
                    return current_directory['size']
                else:
                    current_directory['size'] += write_directories(
                        current_directory[directory], instructions)
            elif (instruction[1] == 'ls'):
                pass
        else:  # directory
            if (instruction[0] == 'dir'):
                dir_name = instruction[1]
                current_directory[dir_name] = {'files': [], 'size': 0}
            else:  # file
                size = int(instruction[0])
                name = instruction[1]
                current_directory['files'].append([name, size])
                current_directory['size'] += size
    return current_directory['size']


def get_file_structure():
    with open('2022/day7/input.txt') as file:
        lines = file.readlines()
        directories = {'/': {'files': [], 'size': 0}, 'size': 0}
        write_directories(directories, lines)
        return directories


def check_directory(directory):
    size = 0
    if (directory['size'] <= 100000):
        size += directory['size']

    for key in directory:
        if (key != 'size' and key != 'files'):
            size += check_directory(directory[key])
    return size


def part1(directories):
    return check_directory(directories['/'])


def possible_directories(directory, freeup_size):
    possibilities = []
    if (directory['size'] >= freeup_size):
        possibilities.append(directory['size'])

    for key in directory:
        if (key != 'size' and key != 'files'):
            possibilities = possibilities + \
                possible_directories(directory[key], freeup_size)
    return possibilities


def part2(directories):
    freeup_size = 30000000 - (70000000 - directories['size'])
    directories_large_enough = possible_directories(
        directories['/'], freeup_size)
    return min(directories_large_enough)


def main():
    file_structure = get_file_structure()
    total_size = part1(directories=file_structure)
    print(total_size)
    directory_size = part2(directories=file_structure)
    print(directory_size)


if __name__ == "__main__":
    main()
