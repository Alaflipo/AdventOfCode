import time 

class Map: 

    def __init__(self, map): 
        self.map: list[list[str]] = map
        self.map_rev: list[list[str]] = [''.join(row) for row in [list(i) for i in zip(*self.map)]]
        self.symmetry = self.check_lines() 
        self.smudges = self.check_smudges()
    
    def check_lines(self): 
        maps = [self.map, self.map_rev]
        for ver, mirror_map in enumerate(maps): 
            for i in range(0, len(mirror_map) - 1): 
                high = i 
                low = i + 1
                symmetry = True 
                while high >= 0 and low < len(mirror_map) and symmetry: 
                    if (mirror_map[high] != mirror_map[low]): 
                        symmetry = False 
                    high -= 1 
                    low += 1
                if (symmetry): 
                    return (ver, i+1) 
    
    def calculate_difference(self, string1, string2): 
        diff = 0 
        for i in range(len(string1)): 
            if string1[i] != string2[i]: 
                diff += 1 
        return diff

    def check_smudges(self): 
        maps = [self.map, self.map_rev]
        for ver, mirror_map in enumerate(maps): 
            for i in range(0, len(mirror_map) - 1): 
                high = i 
                low = i + 1
                possible_smudges = 0  
                while high >= 0 and low < len(mirror_map): 
                    possible_smudges += self.calculate_difference(mirror_map[low], mirror_map[high])
                    high -= 1 
                    low += 1
                if (possible_smudges == 1): 
                    return (ver, i+1) 
    
    def print_reverse(self): 
        for row in self.map_rev: 
            print(row)
        print('\n')

    def __str__(self): 
        output_string = ''
        for row in self.map: 
            output_string += (row + '\n')
        return output_string


def get_input(): 
    with open('./2023/day13/input.txt') as f: 
        maps = [Map(map.split('\n')) for map in f.read()[0:-1].split('\n\n')]
        return maps
    
def part1(input: list[Map]):
    return sum([mp.symmetry[1] if mp.symmetry[0] == 1 else 100 * mp.symmetry[1] for mp in input])

def part2(input: list[Map]): 
    return sum([mp.smudges[1] if mp.smudges[0] == 1 else 100 * mp.smudges[1] for mp in input])

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
