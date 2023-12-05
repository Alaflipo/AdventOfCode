import time 

def get_input(): 
    with open('./2015/day5/input.txt') as f: 
        lines = f.readlines() 
        return [line.strip() for line in lines]
    
def part1(input):
    nice_counter = 0 
    vowels = ['a', 'e', 'i', 'o', 'u']
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for word in input: 
        found_forbidden = False 
        for combo in forbidden: 
            if combo in word: 
                found_forbidden = True 
                break 
        if found_forbidden: continue 
        
        vowel_count = 0 
        double = False 
        for i, char in enumerate(word): 
            if char in vowels: 
                vowel_count += 1
            if (i + 1) < len(word) and char == word[i+1]: 
                double = True
        if (vowel_count >= 3 and double): 
            nice_counter += 1
            
    return nice_counter

def part2(input): 
    nice_counter = 0 
    for word in input: 
        
        doubles = False
        spacing = False 
        for i, char in enumerate(word): 
            if (i + 2) < len(word) and char == word[i+2]: 
                spacing = True 
            if (i + 1) < len(word) and word[i:i+2] in word[i+2:]: 
                doubles += 1
        
        if doubles and spacing: 
            nice_counter += 1 
            
    return nice_counter

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
