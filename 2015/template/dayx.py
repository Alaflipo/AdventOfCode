import time 

def get_input(): 
    with open('./2015/dayx/input.txt') as f: 
        lines = f.readlines() 
        return lines
    
def part1(input):
    
    return 0

def part2(input): 
    return 0

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
