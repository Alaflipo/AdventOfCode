import time 

def get_input(): 
    with open('./2019/day4/input.txt') as f: 
        range = [int(number) for number in f.readlines()[0].strip().split('-')]
        return range
    
def part1(input):
    count = 0 
    for password in range(input[0], input[1]): 
        password = str(password)
        the_same = False
        increasing = True 
        for i in range(0, len(password) - 1): 
            if (password[i] > password[i+1]): 
                increasing = False
                break 
            if (password[i] == password[i+1]):
                the_same = True 
        if (the_same and increasing): 
            count += 1

    return count 

def part2(input): 
    count = 0 
    for password in range(input[0], input[1]): 
        password = str(password)
        the_same = False
        increasing = True 
        for i in range(0, len(password) - 1): 
            if (password[i] > password[i+1]): 
                increasing = False
                break 
            if (password[i] == password[i+1] and 
                ((i + 2) >= len(password) or password[i] != password[i+2]) and 
                ((i-1) < 0 or password[i] != password[i-1])):
                the_same = True 
        if (the_same and increasing): 
            count += 1

    return count 

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
