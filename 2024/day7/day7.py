import time 

def get_input(): 
    with open('./2024/day7/input.txt') as f: 
        lines = f.readlines() 
        answers = []
        numbers = []
        for line in lines: 
            line = line.strip().split(" ")
            answers.append(int(line[0][0:-1]))
            numbers.append([int(number) for number in line[1:]])
        return answers, numbers
    
def find_calibration(current_total, goal, numbers): 
    if (current_total == goal): 
        return True 
    if (len(numbers) == 0): 
        return False 
    
    plus_route = find_calibration(current_total + numbers[0], goal, numbers[1:])
    times_route = find_calibration(current_total * numbers[0], goal, numbers[1:])

    return plus_route or times_route
    
def part1(answers, numbers):
    total_sum = 0 
    for i in range(len(answers)): 
        if find_calibration(numbers[i][0], answers[i], numbers[i][1:]): 
            total_sum += answers[i]
        
    return total_sum


def find_calibration_with_concat(current_total, goal, numbers): 
    if (len(numbers) == 0): 
        if (current_total == goal): 
            return True 
        else: 
            return False 
    
    plus_route = find_calibration_with_concat(current_total + numbers[0], goal, numbers[1:])
    times_route = find_calibration_with_concat(current_total * numbers[0], goal, numbers[1:])
    concat_route = find_calibration_with_concat(int(str(current_total) + str(numbers[0])), goal, numbers[1:])

    return plus_route or times_route or concat_route

def part2(answers, numbers): 
    total_sum = 0 
    for i in range(len(answers)): 
        if find_calibration_with_concat(numbers[i][0], answers[i], numbers[i][1:]): 
            total_sum += answers[i]
        
    return total_sum

def main(): 
    answers, numbers = get_input()
    time_start = time.time() 
    answer = part1(answers, numbers)
    time_end = time.time()
    print('answer part 1:', answer)
    print('running time: ', time_end - time_start, '\n')
    
    time_start = time.time() 
    answer = part2(answers, numbers)
    time_end = time.time()
    print('\nanswer part 2:', answer)
    print('running time: ', time_end - time_start, '\n')

if __name__ == "__main__": 
    main()
