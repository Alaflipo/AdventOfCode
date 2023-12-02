import time 


def get_input(): 
    with open('./2023/day1/input.txt') as f: 
        lines = f.readlines() 
        return [line.strip() for line in lines]
    
def part1(input):
    sum = 0 
    for line in input: 
        numbers = []
        for c in line: 
            if(c.isnumeric()): 
                numbers.append(c)
        sum += int(numbers[0] + numbers[-1])
    return sum

def check_number_strings(line): 
    number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, number in enumerate(number_strings): 
        if number in line: 
            return(str(i+1))
    return -1

def part2(input): 
    sum = 0 
    for line in input: 
        first_last = []
        lines = [line, line[::-1]]
        for l in lines: 
            string_number = ''
            for c in l: 
                if(c.isnumeric()): 
                    first_last.append(c)
                    break 
                else: 
                    string_number += c 
                    result = check_number_strings(string_number)
                    if (result != -1): 
                        first_last.append(result)
                        break 
        sum += int(first_last[0] + first_last[1])
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
