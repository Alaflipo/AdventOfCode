
def read_input(): 
    with open("./day3/input.txt") as f: 
        return [line.strip() for line in f.readlines()]
        

def puzzle1(input): 
    tree_count = 0 
    height = len(input)
    width = len(input[0])
    pos = [0,0]
    while pos[1] < height: 
        if (input[pos[1]][pos[0]] == '#'): tree_count += 1
        pos[0] = (pos[0] + 3) % width
        pos[1] += 1 
    
    return tree_count

def puzzle2(input): 
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counts = 1
    for slope in slopes: 
        tree_count = 0 
        height = len(input)
        width = len(input[0])
        pos = [0,0]
        while pos[1] < height: 
            if (input[pos[1]][pos[0]] == '#'): tree_count += 1
            pos[0] = (pos[0] + slope[0]) % width
            pos[1] += slope[1]
        tree_counts *= tree_count
    return tree_counts

def main(): 
    input = read_input()

    print("result puzzle 1: ")
    result = puzzle1(input)
    print(result) 
    
    print("\nresult puzzle 2: ")
    result = puzzle2(input)
    print(result) 

if __name__ == "__main__": 
    main()
