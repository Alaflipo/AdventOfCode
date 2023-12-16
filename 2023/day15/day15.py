import time 

def get_input(): 
    with open('./2023/day15/input.txt') as f: 
        input = f.read().strip().split(',')
        return input
    
class Box: 

    def __init__(self, i):
        self.box_number = i
        self.lenses: list[tuple[str, int]] = []

    def add(self, label: str, focal_number: int): 
        found = False 
        for i, lens in enumerate(self.lenses): 
            if (lens[0] == label): 
                self.lenses[i] = (label, focal_number)
                found = True 
                break 
        if not found: 
            self.lenses.append((label, focal_number))
    
    def remove(self, label: str): 
        for i, lens in enumerate(self.lenses): 
            if (lens[0] == label): 
                del self.lenses[i]
    
    def calculate_value(self) -> int: 
        sum = 0 
        for i, lens in enumerate(self.lenses): 
            sum += ((self.box_number + 1) * (i + 1) * (lens[1]))
        return sum 
    
    def __str__(self): 
        return '{}'.format(self.lenses)
        

def hash_string(string) -> int: 
    current_value = 0
    for char in string: 
        current_value = (((current_value + ord(char)) * 17) % 256)
    return current_value

def part1(input):
    return sum([hash_string(instruction) for instruction in input])

def part2(input: list[str]): 
    boxes: list[Box] = [Box(i) for i in range(256)]
    for instruction in input: 
        if (instruction[-1] == '-'): 
            label = instruction[0:-1]
            box_number = hash_string(label)
            boxes[box_number].remove(label)
        else: 
            instruction = instruction.split("=")
            label = instruction[0]
            lens = int(instruction[1])
            box_number = hash_string(label)
            boxes[box_number].add(label, lens)
    # for box in boxes: 
    #     print(box)
    return sum([box.calculate_value() for box in boxes])

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
