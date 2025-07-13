import time 

def get_input(): 
    with open('./2024/day5/input.txt') as f: 
        lines = [line.strip() for line in f.readlines()]
        inrules = True 
        rules = []
        prints = []
        for line in lines: 
            if (line == ''): 
                inrules = False
                continue 

            if inrules: 
                rules.append([int(number) for number in line.split('|')])
            else: 
                prints.append([int(number) for number in line.split(',')])

        return rules, prints
    
def convert_dict_rules(rules): 
    rules_dict = {}
    for rule in rules: 
        if str(rule[0]) not in rules_dict.keys(): 
            rules_dict[str(rule[0])] = {'before': [], 'after': []}
        if str(rule[1]) not in rules_dict.keys(): 
            rules_dict[str(rule[1])] = {'before': [], 'after': []}

        rules_dict[str(rule[0])]['after'].append(rule[1])
        rules_dict[str(rule[1])]['before'].append(rule[0])
    return rules_dict
    
def part1(rules, prints):
    middle_numbers = 0 
    rules_dict = convert_dict_rules(rules)

    incorrect_prints = []
    
    for print in prints: 
        mistake = False 
        for i, number in enumerate(print): 
            other_numbers = print[i+1:len(print)]
            for other_number in other_numbers: 
                if other_number in rules_dict[str(number)]['before']: 
                    mistake = True 
                    break 
            if mistake: 
                break 
        if not mistake: 
            middle_numbers += print[int(len(print)/2)]
        else: 
            incorrect_prints.append(print)

    return middle_numbers, incorrect_prints

def part2(rules, prints): 
    rules_dict = convert_dict_rules(rules)
    middle_numbers = 0 

    for p in prints: 
        numbers_before = {}
        for number in p: 
            numbers_before[str(number)] = []

        for i, number in enumerate(p): 
            other_numbers = p[0:i] + p[i+1:len(p)]
            for other_number in other_numbers: 
                if other_number in rules_dict[str(number)]['before']: 
                    numbers_before[str(number)].append(other_number)

        sorted_rules = sorted(numbers_before.items(), key=lambda item: len(item[1]))
        middle_numbers += int(sorted_rules[int(len(sorted_rules)/2)][0])

    return middle_numbers

def main(): 
    rules, prints = get_input()
    time_start = time.time() 
    answer, incorrect_prints = part1(rules, prints)
    time_end = time.time()
    print('answer part 1:', answer)
    print('running time: ', time_end - time_start, '\n')
    
    time_start = time.time() 
    answer = part2(rules, incorrect_prints)
    time_end = time.time()
    print('\nanswer part 2:', answer)
    print('running time: ', time_end - time_start, '\n')

if __name__ == "__main__": 
    main()
