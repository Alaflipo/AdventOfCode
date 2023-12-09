from __future__ import annotations
import time 
import math as math 

class Node(): 
    
    def __init__(self, label): 
        self.left = None 
        self.right = None 
        self.label = label 
    
    def set_left(self, left: Node): 
        self.left = left 
    
    def set_right(self, right: Node): 
        self.right = right 
    
    def ends_in_z(self): 
        return self.label[2] == 'Z'


def get_input(): 
    with open('./2023/day8/input.txt') as f: 
        lines = f.readlines() 
        instructions = lines[0].strip() 
        nodes: dict = {}
        for line in lines[2:]: 
            label = line[0:3]
            nodes[label] = Node(label)
        for line in lines[2:]: 
            label = line[0:3]
            left = line[7:10]
            right = line[12:15]
            nodes[label].set_left(nodes[left])
            nodes[label].set_right(nodes[right])
        
        return [instructions, nodes]
    
def part1(input):
    instructions = input[0]
    nodes = input[1]
    current_node = nodes['AAA']
    instruction_pt = 0 
    steps = 0 
    while current_node.label != 'ZZZ': 
        if (instructions[instruction_pt] == 'L'): 
            current_node = current_node.left
        elif (instructions[instruction_pt] == 'R'):
            current_node = current_node.right
        instruction_pt = (instruction_pt + 1) % len(instructions)
        steps += 1
    return steps 

def all_end_in_z(nodes: list[Node]): 
    for node in nodes: 
        if (not node.ends_in_z()): 
            return False
    return True 

def part2(input): 
    instructions = input[0]
    nodes = input[1]
    current_nodes: list[Node] = [nodes[node_key] for node_key in nodes if node_key[2] == 'A']
    all_steps = 1 
    
    for node in current_nodes: 
        instruction_pt = 0 
        steps = 0 
        current_node = node 
        while not current_node.ends_in_z(): 
            if (instructions[instruction_pt] == 'L'): 
                current_node = current_node.left
            elif (instructions[instruction_pt] == 'R'):
                current_node = current_node.right
            instruction_pt = (instruction_pt + 1) % len(instructions)
            steps += 1
        all_steps = math.lcm(all_steps, steps)
    return all_steps

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
