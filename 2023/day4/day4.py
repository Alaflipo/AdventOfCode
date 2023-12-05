import time 

def get_input(): 
    with open('./2023/day4/input.txt') as f: 
        lines = f.readlines() 
        games = []
        for line in lines: 
            numbers = [number.strip() for number in line.split(":")[1].strip().split("|")]
            games.append([numbers[0].split(" "), numbers[1].split(" "), 1])
        return games 
    
def part1(input):
    sum = 0 
    for game in input: 
        count = 0 
        for number in game[1]: 
            if number != '' and number in game[0]: 
                count += 1
        sum += 2**(count - 1) if count > 0 else 0 
    return sum

def part2(input): 
    sum = 0 
    for i, game in enumerate(input): 
        sum += game[2]
        score = 0 
        for number in game[1]: 
            if number != '' and number in game[0]: 
                score += 1
        for card in range(i + 1, i + 1 + score): 
            input[card][2] += game[2]
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
