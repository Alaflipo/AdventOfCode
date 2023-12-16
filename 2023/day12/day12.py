import time 
from functools import cache

def get_input(): 
    with open('./2023/day12/input.txt') as f: 
        lines = f.readlines()
        data = []
        for line in lines: 
            map = line.split(' ')
            data.append([map[0],  [int(group) for group in map[1].split(',')]])
        return data 

combination_cache = {} 
def find_combinations(hot_spring, groups, size_counter): 
    # Caching wooopp woooppp
    if (hot_spring, groups, size_counter) in combination_cache:
        return combination_cache[(hot_spring, groups, size_counter)] 
    
    # Base cases 
    if hot_spring == '': 
        if (len(groups) == 0 and size_counter == 0): return 1 
        elif (len(groups) == 1 and size_counter == groups[0]): return 1 
        else: return 0 
    if len(groups) > 0 and size_counter > groups[0]: return 0 
    
    number_combinations = 0 
    first_location = hot_spring[0]
    possible_locations = [first_location] if first_location != "?" else ["#", "."]
    for location in possible_locations: 
        if (location == "#"): 
            # We extend the group by one 
            number_combinations += find_combinations(hot_spring[1:], groups, size_counter + 1)
        else: 
            # A group is done so we must do something with the group size 
            if size_counter > 0: 
                if len(groups) > 0 and groups[0] == size_counter:
                    # We have found the correct group 
                    number_combinations += find_combinations(hot_spring[1:], groups[1:], 0)
                else: 
                    # We have not found the correct goup so configuration is wrong! 
                    number_combinations += 0 
            else: 
                # We were not counting a group.. in between groups so just continue 
                number_combinations += find_combinations(hot_spring[1:], groups, 0) 

    combination_cache[(hot_spring, groups, size_counter)] = number_combinations
    return number_combinations

def part1(input):
    global combination_cache
    sum = 0
    for hp_groups in input: 
        hot_springs = hp_groups[0]
        groups = hp_groups[1]
        sum += find_combinations(hot_springs, tuple(groups), 0)
        combination_cache.clear() 
    return sum 

def unfold_springs(hot_springs, groups): 
    uf_hot_springs = hot_springs
    uf_groups = groups.copy()
    for _ in range(4): 
        uf_hot_springs += ('?' + hot_springs)
        uf_groups += groups 
    return uf_hot_springs, uf_groups

def part2(input): 
    global combination_cache
    sum = 0
    for hp_groups in input: 
        hot_springs, groups = unfold_springs(hp_groups[0], hp_groups[1])
        sum += find_combinations(hot_springs, tuple(groups), 0)
        combination_cache.clear()
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
