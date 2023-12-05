import time 
import math 

def get_input(): 
    with open('./2019/day1/input.txt') as f: 
        lines = [int(line.strip()) for line in f.readlines()]
        return lines
    
def part1(input):
    sum = 0 
    for number in input: 
        sum += math.floor(number/3) - 2
    return sum

def part2(input): 
    sum = 0 
    for mass in input: 
        total_fuel = 0 
        fuel = mass  
        while fuel > 0: 
            fuel = math.floor(fuel/3) - 2
            total_fuel += fuel if fuel >= 0 else 0 
        sum += total_fuel
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
