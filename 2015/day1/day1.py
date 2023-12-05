import time 

def get_input(): 
    with open('./2015/day1/input.txt') as f: 
        lines = f.readlines() 
        return lines[0].strip()
    
def part1(input):
    level = 0
    for bracket in input: 
        if bracket == "(": 
            level += 1
        elif(bracket == ")"):
            level -= 1
    return level

def part2(input): 
    level = 0
    for index, bracket in enumerate(input): 
        if bracket == "(": 
            level += 1
        elif(bracket == ")"):
            level -= 1
        if (level < 0): 
            return (index + 1)

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
