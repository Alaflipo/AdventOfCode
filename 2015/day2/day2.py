import time 
from functools import reduce

def get_input(): 
    with open('./2015/day2/input.txt') as f: 
        lines = f.readlines() 
        return [[int(dim) for dim in line.strip().split('x')] for line in lines] 
    
def part1(input):
    total_wrapping = 0
    for box in input: 
        sides = [box[0] * box[-1]]
        for i in range(len(box) - 1): 
            sides.append(box[i] * box[i+1])
        smallest = min(sides)
        total_wrapping += (2 * sum(sides)) + smallest
    return total_wrapping

def part2(input): 
    total_ribon = 0 
    for box in input: 
        box.sort()
        cube = reduce(lambda x,y: x*y, box)
        total_ribon += 2 * box[0] + 2 * box[1] + cube 
    return total_ribon

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
