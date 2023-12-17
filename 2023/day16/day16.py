import time 

def add_loc_dir(loc: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]: 
    return (loc[0] + dir[0], loc[1] + dir[1])

class MirrorMap: 
    
    def __init__(self, map): 
        self.size: tuple[int, int] = (len(map), len(map[0]))
        self.map: list[list[str]] = map 
        self.dir_map: list[list[list[tuple[int, int]]]] = [[[] for _ in range(self.size[1])] for _ in range(self.size[0])] 

    # north: (-1, 0), east: (0, 1), south: (1, 0), west: (0, -1)
    def reflect(self, mirror: str, dir: tuple[int, int]) -> list[tuple[int, int]]: 
        match mirror: 
            case '.': return [dir]
            case '-': 
                if dir[0] != 0: return [(0, 1), (0, -1)]
                else: return [dir]
            case '|': 
                if dir[1] != 0: return [(-1, 0), (1, 0)]
                else: return [dir]
            case '/':
                if (dir == (-1,0)): return [(0,1)]      # north 
                elif (dir == (0,1)): return [(-1,0)]    # east 
                elif (dir == (1,0)): return [(0,-1)]    # south
                elif (dir == (0,-1)): return [(1,0)]    # west
            case '\\': 
                if (dir == (-1,0)): return [(0,-1)]     # north 
                elif (dir == (0,1)): return [(1,0)]     # east 
                elif (dir == (1,0)): return [(0,1)]     # south
                elif (dir == (0,-1)): return [(-1,0)]   # west

    def shoot_beam(self, start_loc: tuple[int, int], start_dir: tuple[int, int]) -> None: 
        self.dir_map = [[[] for _ in range(self.size[1])] for _ in range(self.size[0])] 
        paths_to_explore: list[dict] = [{"loc": start_loc, "dir": start_dir}]
        while len(paths_to_explore) > 0: 
            beam = paths_to_explore.pop()
            # guards 
            if (0 <= beam["loc"][0] < self.size[0] and 0 <= beam["loc"][1] < self.size[1]):  
                if (beam["dir"] in self.dir_map[beam["loc"][0]][beam["loc"][1]]): continue 
                new_beam_dirs = self.reflect(self.map[beam["loc"][0]][beam["loc"][1]], beam["dir"])
                self.dir_map[beam["loc"][0]][beam["loc"][1]].append(beam["dir"])
                for beam_dir in new_beam_dirs: 
                    new_loc = add_loc_dir(beam["loc"], beam_dir)
                    paths_to_explore.append({"loc": new_loc, "dir": beam_dir})
    
    def calculate_beam_number(self): 
        beam_number = 0
        for i in range(self.size[0]): 
            for j in range(self.size[1]): 
                beam_number += (1 if (len(self.dir_map[i][j]) > 0) else 0)
        return beam_number
    
    def __str__(self) -> str:
        output_string = ''
        for i in range(self.size[0]): 
            for j in range(self.size[1]): 
                output_string += ('#' if (len(self.dir_map[i][j]) > 0) else '.')
            output_string += '\n'
        return output_string
             

def get_input(): 
    with open('./2023/day16/input.txt') as f: 
        lines = [[char for char in line.strip()] for line in f.readlines()]
        return MirrorMap(lines)
    
def part1(mirror_map: MirrorMap):
    mirror_map.shoot_beam(start_loc=(0,0), start_dir=(0,1))
    return mirror_map.calculate_beam_number()

def part2(mirror_map: MirrorMap): 
    starts = []
    for i in range(mirror_map.size[0]): 
        starts.append({"loc": (i,0), "dir": (0,1)})
        starts.append({"loc": (i,mirror_map.size[1] - 1), "dir": (0,-1)})
    for j in range(mirror_map.size[1]): 
        starts.append({"loc": (0,j), "dir": (1,0)})
        starts.append({"loc": (mirror_map.size[0] - 1, j), "dir": (1,0)})
    laser_numbers = []
    for start in starts: 
        mirror_map.shoot_beam(start_loc=start["loc"], start_dir=start["dir"])
        laser_number = mirror_map.calculate_beam_number()
        laser_numbers.append(laser_number)
    return max(laser_numbers)

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
