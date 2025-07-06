import time 

def get_input(): 
    with open('./2024/day2/input.txt') as f: 
        lines = f.readlines() 
        reports = [[int(number) for number in line.strip().split(' ')] for line in lines]
        return reports
    

def all_increasing(report: list): 
    for i in range(1, len(report)): 
        if (report[i-1] > report[i]): 
            return False 
    return True 

def all_decreasing(report: list): 
    for i in range(1, len(report)): 
        if (report[i-1] < report[i]): 
            return False 
    return True 

def diff_more_than_three(report: list): 
    for i in range(1, len(report)): 
        if (abs(report[i-1] - report[i]) > 3) or (abs(report[i-1] - report[i]) < 1): 
            return False 
    return True 
    
def check_safe(report: list): 
    return (all_decreasing(report) or all_increasing(report)) and diff_more_than_three(report) 
        
def part1(input):
    safe_reports = 0 
    for report in input: 
        if check_safe(report): 
            safe_reports += 1
    return safe_reports

def part2(input): 
    safe_reports = 0 
    for report in input: 
        if check_safe(report): 
            safe_reports += 1
        else: 
            for i in range(len(report)): 
                if check_safe(report[0:i] + report[i+1:len(report)]): 
                    safe_reports += 1
                    break 
    return safe_reports

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
