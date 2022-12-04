def get_lines(): 
    lines = []

    with open('2022/day3/input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)): 
            lines[i] = lines[i].strip()
    return lines 

def part1(lines):
    total_score = 0
    for rugsack in lines:
        compartment1 = rugsack[0:int(len(rugsack)/2)]
        compartment2 = rugsack[int(len(rugsack)/2):int(len(rugsack))]
        letter = ''
        for i in compartment1:
            if i in compartment2:
                letter = i
                break
        alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        score = alfabet.index(letter) + 1
        total_score += score
        
    return total_score

def part2(lines):
    k = 0
    total_score = 0
    alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while k < len(lines):
        for i in (lines[k]):
            if i in lines[k+1] and i in lines[k+2]:
                score = alfabet.index(i) + 1
                total_score += score
                break
        k += 3
    return total_score



def main(): 
    lines = get_lines()
    answer_part1 = part1(lines)
    print(answer_part1)
    answer_part2 = part2(lines)
    print(answer_part2)

if __name__ == "__main__": 
    main()