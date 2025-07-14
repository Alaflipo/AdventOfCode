from __future__ import annotations
import time 


class Cell: 

    def __init__(self, character, y_pos, x_pos):
        self.x_pos: int = x_pos
        self.y_pos: int = y_pos
        self.frequency: str = character if character != '.' else None 

        self.antinode: bool = False 
        self.antennas: list[tuple[Cell, Cell]] = [] 

    def get_location(self) -> tuple[int, int] : 
        return (self.y_pos, self.x_pos)
    
    def add_antinode(self, antennas: tuple[Cell, Cell]): 
        self.antennas.append(antennas)
        if self.antinode: 
            return 0 
        else: 
            self.antinode = True 
            return 1 

    @staticmethod
    def equal_location(cell: Cell, location: tuple[int, int]): 
        return cell.y_pos == location[0] and cell.x_pos == location[1]
    
    @staticmethod 
    def within_bounds(loc: tuple[int, int], height: int, width: int) -> bool:
        return loc[0] >= 0 and loc[0] < height and loc[1] >= 0 and loc[1] < width

    @staticmethod
    def check_possible(cell: Cell, other: Cell, direction: tuple[int, int], height: int, width: int) -> tuple[int, int]: 
        new_loc = (cell.y_pos + direction[0], cell.x_pos + direction[1])
        if not Cell.equal_location(other, new_loc) and Cell.within_bounds(new_loc, height, width): 
            return new_loc 
        else: 
            return None 
            
    def find_antinodes(self, other: Cell, height: int, width: int) -> list[tuple[int, int]]: 
        antinodes: list[tuple[int, int]] = []
        diff = (self.y_pos - other.y_pos, self.x_pos - other.x_pos) 
        neg_diff = (-1 * diff[0], -1 * diff[1])
        possibilities = [(self, other, diff), (self, other, neg_diff), (other, self, diff), (other, self, neg_diff)]

        for posibility in possibilities: 
            possible = Cell.check_possible(posibility[0], posibility[1], posibility[2], height, width)
            if possible: 
                antinodes.append(possible)

        return antinodes

    def find_resonant(self, other: Cell, height: int, width: int) -> list[tuple[int, int]]: 
        antinodes: list[tuple[int, int]] = []
        diff = (self.y_pos - other.y_pos, self.x_pos - other.x_pos)
        neg_diff = (-1 * diff[0], -1 * diff[1])
        new_loc = self.get_location()
        
        while Cell.within_bounds(new_loc, height, width): 
            antinodes.append(new_loc)
            new_loc = (new_loc[0] + diff[0], new_loc[1] + diff[1])

        new_loc = (self.y_pos + neg_diff[0], self.x_pos + neg_diff[1])
        while Cell.within_bounds(new_loc, height, width): 
            new_loc = (new_loc[0] + neg_diff[0], new_loc[1] + neg_diff[1])
        
        return antinodes
    
    def __str__(self):
        if self.frequency: 
            return self.frequency
        elif self.antinode: 
            return '#'
        else: 
            return '.'

class Grid: 

    def __init__(self, grid: list[list[str]]):
        self.height = len(grid)
        self.width = len(grid[0])
        self.cells: list[list[Cell]] = []
        self.f_types: dict[str, list[Cell]] = {}
        for i in range(self.height): 
            row = []
            for j in range(self.height):
                cell = Cell(grid[i][j], i, j)
                row.append(cell)
                if cell.frequency: 
                    self.add_to_dict(cell)
            self.cells.append(row)

    def add_to_dict(self, cell: Cell): 
        if cell.frequency in self.f_types.keys(): 
            self.f_types[cell.frequency].append(cell)
        else: 
            self.f_types[cell.frequency] = [cell]
    
    def add_antinodes(self): 
        found_antinodes = 0
        for f_type, cells in self.f_types.items(): 
            for i, cell in enumerate(cells): 
                other_cells = cells[:i] + cells[i+1:]
                for other in other_cells: 
                    anti_locations = cell.find_antinodes(other, self.height, self.width)
                    for location in anti_locations: 
                        found_antinodes += self.cells[location[0]][location[1]].add_antinode((cell, other))
        return found_antinodes
    
    def add_resonant_antinodes(self): 
        found_antinodes = 0
        for f_type, cells in self.f_types.items(): 
            for i, cell in enumerate(cells): 
                other_cells = cells[:i] + cells[i+1:]
                for other in other_cells: 
                    anti_locations = cell.find_resonant(other, self.height, self.width)
                    for location in anti_locations: 
                        found_antinodes += self.cells[location[0]][location[1]].add_antinode((cell, other))
        return found_antinodes

    def __str__(self):
        grid_representation = ''
        for i in range(self.height): 
            for j in range(self.height): 
                grid_representation += str(self.cells[i][j])
            grid_representation += '\n'
        return grid_representation

def get_input(): 
    with open('./2024/day8/input.txt') as f: 
        lines = [[char for char in line.strip()] for line in f.readlines()] 
        return lines
    
def part1(input: list[list[str]]):
    grid = Grid(input)
    found_antinodes = grid.add_antinodes()
    return found_antinodes

def part2(input): 
    grid = Grid(input)
    found_antinodes = grid.add_resonant_antinodes()
    print(grid)
    return found_antinodes

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
