def get_lines(): 
    lines = []

    with open('2021/day2/input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)): 
            lines[i] = lines[i].strip()
    return lines 


def part1(lines):
    forward = 0 
    depth = 0
    for line in lines: 
        instruction = line.split(' ')
        direciton = instruction[0]
        value = int(instruction[1])
        if (direciton == 'forward'): 
            forward += value 
        elif (direciton == 'down'): 
            depth += value
        elif (direciton == 'up'): 
            depth -= value
    return forward * depth


def part2(lines): 
    forward = 0 
    depth = 0
    aim = 0
    for line in lines: 
        instruction = line.split(' ')
        direciton = instruction[0]
        value = int(instruction[1])
        if (direciton == 'forward'): 
            forward += value 
            depth += (aim * value)
        elif (direciton == 'down'): 
            aim += value
        elif (direciton == 'up'): 
            aim -= value
    return forward * depth
        

def main(): 
    lines = get_lines()
    answer_part1 = part1(lines)
    print(answer_part1)
    answer_part2 = part2(lines)
    print(answer_part2)


if __name__ == '__main__': 
    main()