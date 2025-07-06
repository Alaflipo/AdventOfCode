import time 
import sort 

def get_input(): 
    with open('./2024/day1/input.txt') as f: 
        lines = [line.strip().split('   ') for line in f.readlines()] 
        list1 = []
        list2 = []
        for line in lines: 
            list1.append(int(line[0]))
            list2.append(int(line[1]))

        return [list1, list2]
    
def compare_lists(list1, list2): 
    sum = 0 
    for i in range(0, len(list1)): 
        sum += abs(list1[i] - list2[i])
    return sum 

def part1(input):
    list1 = input[0]
    list2 = input[1]
    sort.quicksort(list1)
    sort.quicksort(list2)

    sum = compare_lists(list1, list2)
    
    return sum

def make_dict(A): 
    numbers = {}
    for number in A: 
        if str(number) in numbers: 
            numbers[str(number)] += 1 
        else: 
            numbers[str(number)] = 1
    return numbers

def calc_similarity(list1: list, dict2: dict): 
    similarity = 0 
    for number in list1: 
        multiplier = 0 
        if dict2.get(str(number)): 
            multiplier = dict2.get(str(number))
        similarity += number * multiplier

    return similarity

def part2(input): 
    list1 = input[0]
    list2 = input[1]

    dict2 = make_dict(list2)
    
    similarity = calc_similarity(list1, dict2)

    return similarity

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
