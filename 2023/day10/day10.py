import time 

def get_input(): 
    with open('./2023/day10/input.txt') as f: 
        lines = [line.strip() for line in f.readlines()]
        return lines
    
def find_start(map):
    for i in range(len(map)): 
        for j in range(len(map[i])): 
            if map[i][j] == 'S': 
                return (i,j)
    return None 

def calculate_next_pos(pipe_map, prev_pos, cur_pos, next_pos): 
    pipe = pipe_map[cur_pos[0]][cur_pos[1]]
    match pipe: 
        case '|': 
            next_pos = (cur_pos[0] + 1, cur_pos[1]) if cur_pos[0] + 1 != prev_pos[0] else (cur_pos[0] - 1, cur_pos[1])
        case '-':
            next_pos = (cur_pos[0], cur_pos[1] + 1) if cur_pos[1] + 1 != prev_pos[1] else (cur_pos[0], cur_pos[1] - 1)
        case 'L': 
            next_pos = (cur_pos[0] - 1, cur_pos[1]) if cur_pos[0] - 1 != prev_pos[0] else (cur_pos[0], cur_pos[1] + 1)
        case 'J': 
            next_pos = (cur_pos[0] - 1, cur_pos[1]) if cur_pos[0] - 1 != prev_pos[0] else (cur_pos[0], cur_pos[1] - 1)
        case 'F': 
            next_pos = (cur_pos[0] + 1, cur_pos[1]) if cur_pos[0] + 1 != prev_pos[0] else (cur_pos[0], cur_pos[1] + 1)
        case '7': 
            next_pos = (cur_pos[0] + 1, cur_pos[1]) if cur_pos[0] + 1 != prev_pos[0] else (cur_pos[0], cur_pos[1] - 1)
    return next_pos

def create_loop_map(pipe_map): 
    loop_map = [[0] * len(pipe_map[0]) for _ in range(len(pipe_map))]
    starting_point = find_start(pipe_map)
    loop_map[starting_point[0]][starting_point[1]] = 1
    prev_pos = (starting_point[0], starting_point[1])
    cur_pos = (starting_point[0] + 1, starting_point[1])
    next_pos = None 
    dist = 1
    while cur_pos != starting_point:
        loop_map[cur_pos[0]][cur_pos[1]] = 1
        next_pos = calculate_next_pos(pipe_map, prev_pos, cur_pos, next_pos)
        prev_pos = cur_pos
        cur_pos = next_pos
        dist += 1
    return loop_map, dist 

def part1(pipe_map):
    _, dist = create_loop_map(pipe_map)
    return int(dist/2)

def change_dir(dir, pipe): 
    match pipe: 
        case 'L': 
            new_dir = (-1, 0) if dir[1] == -1 else (0, 1)
        case 'J': 
            new_dir = (-1, 0) if dir[1] == 1 else (0, -1)
        case 'F': 
            new_dir = (1, 0) if dir[1] == -1 else (0, 1)
        case '7': 
            new_dir = (1, 0) if dir[1] == 1 else (0, -1)
        case _: 
            new_dir = dir
    return new_dir

def print_bounds(bounds): 
    for line in bounds: 
        print(line)

def search_empty(animal_bounds, start_point):
    filled = 0 
    positions = [start_point]
    while (len(positions) > 0): 
        pos = positions.pop()
        if (animal_bounds[pos[0]][pos[1]] == 0): 
            filled += 1
        animal_bounds[pos[0]][pos[1]] = 1 
        directions = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
        for dir in directions: 
            if (animal_bounds[dir[0]][dir[1]] == 0): 
                positions.append(dir)
    return filled

def fill_map(animal_bounds, pipe, position, direction): 
    start_points = []
    filled = 0 
    match pipe: 
        case 'L': 
            if (direction == (0, 1)): 
                start_points.append((position[0], position[1] - 1))
                start_points.append((position[0] + 1, position[1]))
        case 'J': 
            if (direction == (-1, 0)): 
                start_points.append((position[0], position[1] + 1))
                start_points.append((position[0] + 1, position[1]))
        case 'F': 
            if (direction == (1, 0)): 
                start_points.append((position[0], position[1] - 1))
                start_points.append((position[0] - 1, position[1]))
        case '7': 
            if (direction == (0, -1)): 
                start_points.append((position[0], position[1] + 1))
                start_points.append((position[0] - 1, position[1]))
        case '|': 
            if (direction == (-1, 0)): 
                start_points.append((position[0], position[1] + 1))
            else: 
                start_points.append((position[0], position[1] - 1))
        case '-': 
            if (direction == (0, 1)): 
                start_points.append((position[0] + 1, position[1]))
            else: 
                start_points.append((position[0] - 1, position[1]))
    for sp in start_points: 
        if animal_bounds[sp[0]][sp[1]] == 0: 
            filled += search_empty(animal_bounds, sp)
    return filled 


def part2(pipe_map): 
    animal_bounds, _ = create_loop_map(pipe_map)
    starting_point = find_start(pipe_map)
    prev_pos = (starting_point[0], starting_point[1])
    cur_pos = (starting_point[0] - 1, starting_point[1])
    dir = (-1, 0)
    next_pos = None 
    filled = 0
    while cur_pos != starting_point:
        pipe = pipe_map[cur_pos[0]][cur_pos[1]]
        dir = change_dir(dir, pipe)
        filled += fill_map(animal_bounds, pipe, cur_pos, dir)
        next_pos = calculate_next_pos(pipe_map, prev_pos, cur_pos, next_pos)
        prev_pos = cur_pos
        cur_pos = next_pos
        next_pos = None 
    return filled 

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
