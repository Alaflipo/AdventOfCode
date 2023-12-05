import time 
import hashlib

def get_input(): 
    with open('./2015/day4/input.txt') as f: 
        lines = f.readlines() 
        return lines[0].strip()
    
def part1(input):
    number = 0
    found = False 
    while not found: 
        number += 1
        code = input + str(number)
        result = hashlib.md5(code.encode())
        if result.hexdigest()[0:5] == '00000': 
            found = True 
    return number

def part2(input): 
    number = 0
    found = False 
    while not found: 
        number += 1
        code = input + str(number)
        result = hashlib.md5(code.encode())
        if result.hexdigest()[0:6] == '000000': 
            found = True 
    return number

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
