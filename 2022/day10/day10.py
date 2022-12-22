
def get_instructions():
    with open('2022/day10/input.txt') as file:
        lines = file.readlines()
        instructions = []
        for line in lines:
            instructions.append(line.strip().split(' '))
        return instructions


def part1(instructions):
    clock = 1
    register = 1
    score = 0
    for instruction in instructions:
        if instruction[0] == 'addx':
            for _ in range(2):
                if (clock + 20) % 40 == 0:
                    score += register * clock
                clock += 1
            register += int(instruction[1])
        else:
            if (clock + 20) % 40 == 0:
                score += register * clock
            clock += 1
    return score


def part2(instructions):
    crt = [['🌲' for _ in range(40)] for _ in range(6)]
    register = 1
    instruction_idx = 0
    wait = 0
    for clock in range(240):

        if (abs(register - (clock % 40)) <= 1):
            crt[int(clock / 40)][clock % 40] = '🎁'

        if instructions[instruction_idx][0] == 'addx':
            if (wait == 1):
                register += int(instructions[instruction_idx][1])
                instruction_idx += 1
                wait = 0
            else:
                wait += 1
        else:
            instruction_idx += 1
    crt_string = ''
    for row in crt:
        crt_string += (''.join(row) + '\n')
    return crt_string


def main():
    instructions = get_instructions()
    score = part1(instructions)
    print(score)
    crt_output = part2(instructions)
    print(crt_output)


if __name__ == "__main__":
    main()
