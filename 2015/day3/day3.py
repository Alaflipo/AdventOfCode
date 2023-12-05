import time 

def get_input(): 
    with open('./2015/day3/input.txt') as f: 
        lines = f.readlines() 
        return lines[0].strip()
    
def add_location(new, locations): 
    if new[0] not in locations:
        locations[new[0]] = {new[1]}
    else: 
        locations[new[0]].add(new[1])
    return locations

def part1(input):
    locations = {0: {0}}
    last = [0, 0]
    for dir in input: 
        new = []
        match dir: 
            case "^": 
                new = [last[0], last[1] + 1]
                locations = add_location(new, locations)
            case "v": 
                new = [last[0], last[1] - 1]
                locations = add_location(new, locations)
            case ">": 
                new = [last[0] + 1, last[1]]
                locations = add_location(new, locations)
            case "<": 
                new = [last[0] - 1, last[1]]
                locations = add_location(new, locations)
        last = new
    sum = 0 
    for key in locations: 
        sum += len(locations[key])
    return sum

def part2(input): 
    locations = {0: {0}}
    last_locs = [[0, 0], [0,0]]
    s = 0 
    for dir in input: 
        new = []
        match dir: 
            case "^": 
                new = [last_locs[s][0], last_locs[s][1] + 1]
                locations = add_location(new, locations)
            case "v": 
                new = [last_locs[s][0], last_locs[s][1] - 1]
                locations = add_location(new, locations)
            case ">": 
                new = [last_locs[s][0] + 1, last_locs[s][1]]
                locations = add_location(new, locations)
            case "<": 
                new = [last_locs[s][0] - 1, last_locs[s][1]]
                locations = add_location(new, locations)
        last_locs[s] = new
        s = (s + 1) % 2
    sum = 0 
    for key in locations: 
        sum += len(locations[key])
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
