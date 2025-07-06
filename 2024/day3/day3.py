import time 

def get_input(): 
    with open('./2024/day3/input.txt') as f: 
        lines = f.readlines() 
        instructions = [line.strip() for line in lines]
        instruction = ''
        for ins in instructions: 
            instruction += ins
        return instruction
    
def get_mult_instructs(message: str) -> list: 
    mult_instructs = []
    for i in range(len(message)): 
        if message[i] == '(' and message[i-3:i] == 'mul':
            numbers_comma = message[i+1:i+9].split(')')[0]
            numbers = numbers_comma.split(',')
            if len(numbers) == 2 and numbers[0].isnumeric() and len(numbers[0]) <= 3 and numbers[1].isnumeric() and len(numbers[1]) <= 3: 
                mult_instructs += [[int(numbers[0]), int(numbers[1])]]
    
    return mult_instructs

def calc_mult_instructs(instructs):
    total_mult = 0 
    for mult_instruct in instructs: 
        total_mult += mult_instruct[0] * mult_instruct[1]
    return total_mult

def part1(input):
    mult_instructs = get_mult_instructs(input)
    return calc_mult_instructs(mult_instructs)

def get_mult_instructs_2(message: str): 
    mult_instructs = []
    do = True 
    for i in range(len(message)): 
        if message[i] == '(' and message[i-3:i] == 'mul' and do:
            numbers_comma = message[i+1:i+9].split(')')[0]
            numbers = numbers_comma.split(',')
            if len(numbers) == 2 and numbers[0].isnumeric() and len(numbers[0]) <= 3 and numbers[1].isnumeric() and len(numbers[1]) <= 3: 
                mult_instructs += [[int(numbers[0]), int(numbers[1])]]

        if message[i] == 'd' and message[i:i+4] == 'do()': 
            do = True
        elif message[i] == 'd' and message[i:i+7] == 'don\'t()': 
            do = False
    
    return mult_instructs

def part2(input): 
    mult_instructs = get_mult_instructs_2(input)
    return calc_mult_instructs(mult_instructs)

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
