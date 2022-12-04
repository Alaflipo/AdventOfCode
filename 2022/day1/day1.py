

def get_lines(): 
    lines = []

    with open('2022/day1/input.txt') as f:
        lines = f.readlines()
    return lines 

def part1(lines): 
    
    elves = []
    sum = 0
    for line in lines: 
        colories = line.strip()
        if (colories == ''): 
            elves.append(sum)
            sum = 0
        else: 
            sum += int(colories)

    print(max(elves))

def part2(lines):
    elves = []
    sum = 0
    for line in lines: 
        colories = line.strip()
        if (colories == ''): 
            elves.append(sum)
            sum = 0
        else: 
            sum += int(colories)
    
    elves.sort()
    calories_top_3 = elves[-1] + elves[-2] + elves[-3]
    print(calories_top_3)


def main(): 
    lines = get_lines()
    part1(lines)
    part2(lines)

if __name__ == "__main__": 
    main()
    