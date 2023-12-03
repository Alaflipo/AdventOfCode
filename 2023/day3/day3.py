import time 

def get_input(): 
    with open('./2023/day3/input.txt') as f: 
        lines = [line.strip() for line in f.readlines()]
        return lines 

def find_special(ver, hor, input): 
    for i in range(ver[0], ver[1] + 1): 
        for j in range(hor[0], hor[1] + 1): 
            if not input[i][j].isnumeric() and input[i][j] != '.': 
                return True
    return False

def find_number(j, line): 
    while j >= 0 and line[j].isnumeric(): 
        j -= 1 
    start = j + 1
    end = start 
    while end < len(line) and line[end].isnumeric(): 
        end += 1
    return end, int(line[start:end])

def find_numbers(ver, hor, input): 
    numbers = []
    for i in range(ver[0], ver[1] + 1): 
        j = hor[0]
        while j <= hor[1]: 
            if input[i][j].isnumeric(): 
                new_j, number = find_number(j, input[i])
                j = new_j
                numbers.append(number)
            else: 
                j += 1
    print(numbers)
    return numbers 



def find_range(n, m, i, j): 
    left = (j - m - 1) if (j - m - 1) >= 0 else (j - m)
    up = (i - 1) if (i - 1) >= 0 else i
    right = j 
    down = (i + 1) if (i + 1) < n else i 
    return [up, down], [left, right]
    
def part1(input):
    sum = 0 
    n = len(input)
    for i, line in enumerate(input): 
        number = ''
        for j, char in enumerate(line): 
            if (char.isnumeric()): 
                number += char
            elif(number != ''): 
                m = len(number)
                ver, hor = find_range(n, m, i, j)
                if find_special(ver, hor, input): 
                    sum += int(number)
                number = ''
        if len(number) > 0: 
            ver, hor = find_range(n, m, i, j)
            if find_special(ver, hor, input): 
                sum += int(number)
    return sum


def part2(input): 
    sum = 0 
    n = len(input)
    for i, line in enumerate(input): 
        for j, char in enumerate(line): 
            if char == '*':
                ver, hor = find_range(n, 1, i, j + 1) 
                numbers = find_numbers(ver, hor, input)
                if (len(numbers) == 2): 
                    sum += (numbers[0] * numbers[1])
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
