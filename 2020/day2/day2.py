
def read_input(): 
    passwords = []
    with open("./day2/input.txt") as f: 
        lines = f.readlines()
        for line in lines: 
            data = line.split(" ")
            range = [int(number) for number in data[0].split("-")]
            letter = data[1][0]
            password = data[2].strip()
            passwords.append([letter, range, password])
    return passwords 

def puzzle1(input): 
    correct = 0 
    for type in input: 
        count = 0 
        for letter in type[2]: 
            if type[0] == letter: 
                count += 1
        if (count >= type[1][0] and count <= type[1][1]): 
            correct += 1 
    return correct 

def puzzle2(input): 
    correct = 0 
    for type in input: 
        if ((type[2][type[1][0] - 1] == type[0] or type[2][type[1][1] - 1] == type[0]) and 
            not (type[2][type[1][0] - 1] == type[0] and type[2][type[1][1] - 1] == type[0])): 
            correct += 1
    return correct 

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
