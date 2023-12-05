import time 

def get_input(): 
    with open('./2019/day2/input.txt') as f: 
        program = [int(number) for number in f.readlines()[0].strip().split(',')]
        return program
    
def part1(input):
    program = input.copy()
    program[1] = 12
    program[2] = 2
    pointer = 0 
    stop = False 
    while pointer < len(program) and not stop: 
        match program[pointer]: 
            case 1: 
                program[program[pointer + 3]] = program[program[pointer + 1]] + program[program[pointer + 2]]
            case 2: 
                program[program[pointer + 3]] = program[program[pointer + 1]] * program[program[pointer + 2]]
            case 99: 
                stop = True 
        pointer += 4
    return program[0]

def part2(input): 
    noun = 0
    verb = 0
    p = input.copy()
    while p[0] != 19690720: 
        if (noun >= 100): 
            verb += 1
            noun = 0 
        else: 
            noun += 1 
        p = input.copy()
        p[1] = noun
        p[2] = verb
        pointer = 0 
        stop = False 
        while pointer < len(p) and not stop: 
            match p[pointer]: 
                case 1: 
                    p[p[pointer + 3]] = p[p[pointer + 1]] + p[p[pointer + 2]]
                case 2: 
                    p[p[pointer + 3]] = p[p[pointer + 1]] * p[p[pointer + 2]]
                case 99: 
                    stop = True 
            pointer += 4

    return 100 * noun + verb 

def main(): 
    input = get_input()
    time_start = time.time() 
    answer = part1(input)
    time_end = time.time()
    print('answer part 1:', answer)
    print('running time: ', time_end - time_start, '\n')
    
    time_start = time.time() 
    answer = part2(input)
    time_end = time.time()
    print('\nanswer part 2:', answer)
    print('running time: ', time_end - time_start, '\n')

if __name__ == "__main__": 
    main()
