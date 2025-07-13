import time 

def get_input(): 
    with open('./2024/day4/input.txt') as f: 
        lines = f.readlines() 
        matrix = [line.strip() for line in lines]
        return matrix

def check_bounds(size, variable): 
    return variable >= 0 and variable < size 

def check_direction(input, start_x, start_y, dx, dy, word): 
    size_y = len(input)
    size_x = len(input[0])

    if not (check_bounds(size_x, start_x + dx * (len(word) - 1)) and check_bounds(size_y, start_y + dy * (len(word) - 1))):
        return 0
    
    for i in range(len(word)): 
        if input[start_y + dy * i][start_x + dx * i] != word[i]: 
            return 0 
        
    return 1 

def part1(input):
    total_xmas = 0 
    word = 'XMAS'
    width = len(input[0])
    height = len(input)

    for i in range(height): 
        for j in range(width): 
            if input[i][j] == word[0]: 
                total_xmas += check_direction(input, j, i, 0, -1, word) #North 
                total_xmas += check_direction(input, j, i, 1, -1, word) #North East  
                total_xmas += check_direction(input, j, i, 1, 0, word) #East
                total_xmas += check_direction(input, j, i, 1, 1, word) #South East  
                total_xmas += check_direction(input, j, i, 0, 1, word) #South 
                total_xmas += check_direction(input, j, i, -1, 1, word) #South West  
                total_xmas += check_direction(input, j, i, -1, 0, word) #West
                total_xmas += check_direction(input, j, i, -1, -1, word) #North West 
    return total_xmas


def mas_pos(input, i, j): 
    return (input[i-1][j-1] == 'M' and input[i+1][j+1] == 'S') or (input[i-1][j-1] == 'S' and input[i+1][j+1] == 'M')

def mas_neg(input, i, j): 
    return (input[i+1][j-1] == 'M' and input[i-1][j+1] == 'S') or (input[i+1][j-1] == 'S' and input[i-1][j+1] == 'M')

def part2(input): 
    total_xmas = 0 
    width = len(input[0])
    height = len(input)

    for i in range(1, height - 1): 
        for j in range(1, width - 1): 
            if input[i][j] == 'A': 
                if mas_pos(input, i, j) and mas_neg(input, i, j): 
                    total_xmas += 1

    return total_xmas

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
