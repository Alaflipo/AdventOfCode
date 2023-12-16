import time 
import copy

def add_loc(loc: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]: 
    return (loc[0] + dir[0], loc[1] + dir[1])

def print_map(map) -> str:
    output_string = ''
    for row in map: 
        for char in row: 
            output_string += char
        output_string += '\n'
    output_string += '\n'
    print(output_string)

class Map: 

    def __init__(self, lines): 
        self.size: tuple[int] = (len(lines), len(lines[0]))
        self.map: list[list[str]] = lines 
        self.rocks: list[tuple[int, int]] = []
        self.find_rocks()

    def find_rocks(self) -> list[tuple[int, int]]: 
        for i in range(len(self.map)): 
            for j in range(len(self.map[0])): 
                if (self.map[i][j] == 'O'): 
                    self.rocks.append((i, j))
    
    def calculate_load(self) -> int: 
        load = 0 
        for rock in self.rocks: 
            load += self.size[0] - rock[0]
        return load 
    
    def loc_within_map(self, loc: tuple[int, int]): 
        return 0 <= loc[0] < self.size[0] and 0 <= loc[1] < self.size[1]
    
    def __str__(self) -> str:
        output_string = ''
        for row in self.map: 
            for char in row: 
                output_string += char
            output_string += '\n'
        output_string += '\n'
        return output_string
    
    # north: (-1, 0), east: (0, 1), south: (1, 0), west: (0, -1)
    def roll_rocks_dir(self, direction: tuple[int, int]) -> None: 
        # Sort them based on the direction so we handle them in the right order (rocks don't block each other)
        self.rocks.sort(key=lambda x: x[0] if direction[0] != 0 else x[1], reverse=(direction[0] > 0 or direction[1] > 0))
        for i, rock_loc in enumerate(self.rocks):
            self.map[rock_loc[0]][rock_loc[1]] = '.'
            current_loc = rock_loc
            next_loc = add_loc(current_loc, direction)
            while self.loc_within_map(next_loc): 
                if (self.map[next_loc[0]][next_loc[1]] == '.'): 
                    current_loc = next_loc
                    next_loc = add_loc(current_loc, direction)
                else: break 
            self.map[current_loc[0]][current_loc[1]] = 'O'
            self.rocks[i] = current_loc

def get_input(): 
    with open('./2023/day14/input.txt') as f: 
        lines = [[char for char in line.strip()] for line in f.readlines()] 
        return Map(lines)
    
def part1(map: Map):
    map.roll_rocks_dir((-1,0))
    load = map.calculate_load()
    return load 

def part2(map: Map):
    maps = [[row[:] for row in map.map]]
    loop_start = 0
    loop_end = 0  
    for i in range(1000000000): 
        map.roll_rocks_dir((-1, 0)) 
        map.roll_rocks_dir((0, -1)) 
        map.roll_rocks_dir((1, 0)) 
        map.roll_rocks_dir((0, 1)) 
        for start, map_prev in enumerate(maps): 
            if map_prev == map.map:
                loop_start = start 
                loop_end = i + 1
                break 
        maps.append([row[:] for row in map.map])
        if (loop_end > 0): break 
    # We have found from where a loop begins so we check how many iterations we still have to go 
    cycle_until = (1000000000 - loop_start) % (loop_end - loop_start)
    for i in range(cycle_until): 
        map.roll_rocks_dir((-1, 0)) 
        map.roll_rocks_dir((0, -1)) 
        map.roll_rocks_dir((1, 0)) 
        map.roll_rocks_dir((0, 1)) 
    return map.calculate_load()

def main(): 
    input = get_input()
    time_start = time.time() 
    answer = part1(copy.deepcopy(input))
    time_end = time.time()
    print('answer part 1:', answer)
    print('running time: ', time_end - time_start, '\n')
    
    time_start = time.time() 
    answer = part2(copy.deepcopy(input))
    time_end = time.time()
    print('\nanswer part 2:', answer)
    print('running time: ', time_end - time_start, '\n')

if __name__ == "__main__": 
    main()
