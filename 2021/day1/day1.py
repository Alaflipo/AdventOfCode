def get_lines(): 
    lines = []

    with open('2021/day1/input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)): 
            lines[i] = int(lines[i].strip())
    return lines 


def part1(lines):
    count = 0 
    for idx, line in enumerate(lines): 
        if (idx == 0): 
            continue 
        depth = line
        previous_depth = lines[idx - 1]
        if depth > previous_depth: 
            count += 1
    print(count)


def part2(lines): 
    count = 0 
    previous_sum = lines[0] + lines[1] + lines[2]
    idx = 1 
    while idx < len(lines) - 2: 
        sum = lines[idx] + lines[idx + 1] + lines[idx + 2]
        if sum > previous_sum: 
            count += 1
        previous_sum = sum
        idx += 1
    print(count)
        

def main(): 
    lines = get_lines()
    part1(lines)
    part2(lines)


if __name__ == '__main__': 
    main()