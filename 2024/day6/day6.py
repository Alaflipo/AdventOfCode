import time 


class Cell: 
    
    def __init__(self, i: int, j: int, type: str):
        self.x = j
        self.y = i
        self.type = type 
        

        self.visited = False 
        self.looping = False 
        self.directions: list[tuple[int, int]] = []

    def change_type(self, new_type): 
        self.type = new_type

    def visit(self, direction: tuple[int, int]) -> bool: 
        self.visited = True 
        self.type = 'X'

        if direction in self.directions: 
            self.looping = True 
        
        self.directions.append(direction)
        

    def reset(self): 
        if self.type != "#": 
            self.type == '.'
        self.directions = []
        self.visited = False 
        self.looping = False 
    
    @staticmethod
    def change_dir(old_dir) -> tuple[int, int]: 
        match (old_dir): 
            case (0, -1): 
                return (1, 0)
            case (1, 0): 
                return (0, 1)
            case (0, 1): 
                return (-1, 0) 
            case (-1, 0): 
                return (0, -1)
            case _: 
                return (0, -1)

class Ground: 

    def __init__(self, layout: list[list[str]]):
        self.layout: list[list[Cell]] = []
        self.height: int = len(layout)
        self.width: int = len(layout[0])
        
        for i, line in enumerate(layout): 
            ground_line = []
            for j, pos in enumerate(line): 
                ground_line.append(Cell(i, j, pos))
            self.layout.append(ground_line)
        
        self.start_cell: Cell = self.find_startpos()
        self.inserted_object: Cell = self.layout[0][0]

    def within_bounds(self, x_index, y_index) -> bool: 
        return ((x_index >= 0 and x_index < self.width) and (y_index > 0 and y_index < self.height))
    
    def find_startpos(self) -> tuple[int, int]: 
        for i, line in enumerate(self.layout): 
            for j, cell in enumerate(line): 
                if cell.type == '^': 
                    cell.visit((0, -1))
                    return self.layout[i][j]
    
    def reset(self): 
        self.inserted_object.type = '.'
        for row in self.layout: 
            for cell in row: 
                cell.reset()
        self.start_cell.visit((0, -1))
        

    def insert_object(self, i: int, j: int): 
        self.layout[i][j].change_type("#")
        self.inserted_object = self.layout[i][j]
    
    def walk(self): 
        current_cell: Cell = self.start_cell
        dir = (0, -1)
        walked_spots = []
        in_bound = True  
        new_pos = (0, 0)

        while in_bound and not current_cell.looping: 
            if not self.within_bounds(current_cell.x + dir[0], current_cell.y + dir[1]): 
                in_bound = False 
                break 

            possible_step = False 
            new_pos = (0, 0) 
            while not possible_step: 
                new_pos = (current_cell.x + dir[0], current_cell.y + dir[1])

                # check if we found a box  
                if self.layout[new_pos[1]][new_pos[0]].type == "#": 
                    dir = Cell.change_dir(dir)
                else: 
                    possible_step = True 
        
            # take step 
            current_cell = self.layout[new_pos[1]][new_pos[0]] 
            if current_cell.type != 'X': 
                walked_spots.append((new_pos[1], new_pos[0]))

            current_cell.visit(dir)
        
        return (walked_spots, current_cell.looping)

def get_input(): 
    with open('./2024/day6/input.txt') as f: 
        lines = [line.strip() for line in f.readlines()]
        return lines

def part1(lines):
    ground = Ground(lines)

    walked_spots, _ = ground.walk()
    return len(walked_spots)

def part2(input): 
    ground = Ground(input)
    loop_count = 0 
    possible_spots, _ = ground.walk()

    for i, j in possible_spots: 
        if (ground.layout[i][j].type != '#') and (ground.layout[i][j] != ground.start_cell): 
            ground.insert_object(i,j)
            _, looping = ground.walk()
            loop_count += looping 
            print(loop_count)
            ground.reset()

    return loop_count

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
