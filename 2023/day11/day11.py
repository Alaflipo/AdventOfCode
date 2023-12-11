import time 

class GalaxyMap: 

    def __init__(self, gm): 
        self.gm: list[list[str]] = gm
        self.height = len(gm)
        self.width = len(gm[0])
        self.expand_columns = []
        self.expand_rows = []
        self.galaxies = [] 
        self.search_galaxies()

    def search_galaxies(self): 
        for i in range(self.height): 
            for j in range(self.width): 
                if (self.gm[i][j] == "#"): 
                    self.galaxies.append((i, j))
    
    def check_columns(self):
        for j in range(self.width): 
            found_unisverse = False 
            for i in range(self.height): 
                if (self.gm[i][j] == '#'): 
                    found_unisverse = True 
                    break 
            if (not found_unisverse): 
                self.expand_columns.append(j)
    
    def check_rows(self): 
        for i in range(self.height): 
            found_unisverse = False 
            for j in range(self.width): 
                if (self.gm[i][j] == '#'): 
                    found_unisverse = True 
                    break 
            if (not found_unisverse): 
                self.expand_rows.append(i) 

    def expand(self):
        self.check_rows()
        self.check_columns()
    
    def calc_distances_galaxies(self, expand_value): 
        sum = 0
        for i, g1 in enumerate(self.galaxies): 
            for j, g2 in enumerate(self.galaxies): 
                if (i == j): break 
                expanded = 0 
                for c in self.expand_columns: 
                    if ((c < g1[1] and c > g2[1]) or (c < g2[1] and c > g1[1])): 
                        expanded += (expand_value - 1)
                for r in self.expand_rows: 
                    if ((r < g1[0] and r > g2[0]) or (r < g2[0] and r > g1[0])): 
                        expanded += (expand_value - 1) 
                sum += (abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + expanded)
        return sum 


def get_input(): 
    with open('./2023/day11/input.txt') as f: 
        lines = [[char for char in line.strip()] for line in f.readlines()]
        gm = GalaxyMap(lines)
        gm.expand()
        return gm 
    
# 9724940
def part1(galaxy_map: GalaxyMap):
    return galaxy_map.calc_distances_galaxies(2)

def part2(galaxy_map: GalaxyMap): 
    return galaxy_map.calc_distances_galaxies(1000000)

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
