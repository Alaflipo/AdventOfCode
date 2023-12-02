
def read_input(): 

    with open("./day1/input.txt") as f: 
        lines = f.readlines()
        expenses = [int(line.strip()) for line in lines]
        return expenses

def puzzle1(input): 
    for i, e1 in enumerate(input): 
        for j, e2 in enumerate(input): 
            if (i == j): continue 
            if (e1 + e2 == 2020): return e1 * e2

def puzzle2(input): 
    for i, e1 in enumerate(input): 
        for j, e2 in enumerate(input): 
            for k, e3 in enumerate(input): 
                if (i == j or j == k or i == k): continue 
                if (e1 + e2 + e3 == 2020): return e1 * e2 * e3

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
