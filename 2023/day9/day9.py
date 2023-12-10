import time 

def get_input(): 
    with open('./2023/day9/input.txt') as f: 
        lines = [[int(number) for number in line.strip().split(' ')] for line in f.readlines()]
        return lines
    
def all_zero(sequence): 
    for number in sequence: 
        if (number != 0): return False 
    return True 

def predict_next(last, current): 
    return current[-1] + last[-1]

def predict_prev(last, current): 
    return current[0] - last[0]

def part1(input):
    sum = 0 
    for sequence in input: 
        difs: list[list] = [sequence]
        while (not all_zero(difs[-1])): 
            difference = []
            for i in range(len(difs[-1]) - 1): 
                difference.append(difs[-1][i+1] - difs[-1][i])
            difs.append(difference)
        difs[-1].append(0)
        for i in range(len(difs) - 2, -1, -1):
            difs[i].append(predict_next(difs[i+1], difs[i]))
        sum += difs[0][-1] 
    return sum

def part2(input): 
    sum = 0 
    for sequence in input: 
        difs: list[list] = [sequence]
        while (not all_zero(difs[-1])): 
            difference = []
            for i in range(len(difs[-1]) - 1): 
                difference.append(difs[-1][i+1] - difs[-1][i])
            difs.append(difference)
        difs[-1].append(0)
        for i in range(len(difs) - 2, -1, -1):
            difs[i].insert(0, predict_prev(difs[i+1], difs[i]))
        sum += difs[0][0] 
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
