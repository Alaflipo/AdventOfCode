import time 

def process_instruction(instruction): 
    c1 = instruction[0].split(',')
    c2 = instruction[2].split(',')
    # y, x, height, width 
    return [int(c1[1]), int(c1[0]), (int(c2[1]) - int(c1[1])), (int(c2[0]) - int(c1[0]))]


def get_input(): 
    with open('./2015/day6/input.txt') as f: 
        lines = f.readlines() 
        instructions = []
        for line in lines: 
            instruction = line.strip().split(' ')
            if (len(instruction) == 4): 
                instructions.append(['toggle', process_instruction(instruction[1:])])
            elif (instruction[1] == 'on'): 
                instructions.append(['on', process_instruction(instruction[2:])])
            else:
                instructions.append(['off', process_instruction(instruction[2:])])
        return instructions
    
def part1(input):
    lamps = [ [False]*1000 for i in range(1000)]
    for inst in input:
        for i in range(inst[1][0], inst[1][0] + inst[1][2] + 1): 
            for j in range(inst[1][1], inst[1][1] + inst[1][3] + 1): 
                match inst[0]: 
                    case 'toggle': lamps[i][j] = not lamps[i][j]
                    case 'on': lamps[i][j] = True 
                    case 'off': lamps[i][j] = False 
    sum = 0 
    for row in lamps: 
        for lamp in row: 
            if (lamp): sum += 1 
    return sum 

def part2(input): 
    lamps = [ [0] * 1000 for _ in range(1000)]
    for inst in input:
        for i in range(inst[1][0], inst[1][0] + inst[1][2] + 1): 
            for j in range(inst[1][1], inst[1][1] + inst[1][3] + 1): 
                match inst[0]: 
                    case 'toggle': lamps[i][j] += 2
                    case 'on': lamps[i][j] += 1
                    case 'off': lamps[i][j] = lamps[i][j] - 1 if lamps[i][j] > 0 else 0 
    sum = 0 
    for row in lamps: 
        for lamp in row: 
            sum += lamp
    return sum 

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
