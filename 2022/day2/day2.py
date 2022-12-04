def get_lines(): 
    lines = []

    with open('2022/day2/input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)): 
            lines[i] = lines[i].strip()
    return lines 

def part1(lines): 
    plays_opponent = ['A', 'B', 'C']
    plays_player = ['X', 'Y', 'Z']
    total_score = 0
    for line in lines: 
        strategies = line.split(' ')
        opponent = strategies[0]
        opponent_idx = plays_opponent.index(opponent)

        player = strategies[1]
        player_idx = plays_player.index(player)

        score = player_idx + 1
        if (plays_player[(opponent_idx + 1) % 3] == player):
            score += 6
        elif (plays_player[(opponent_idx) % 3] == player):
            score += 3
        
        total_score += score 
    
    return total_score
        
def part2(lines):
    plays_opponent = ['A', 'B', 'C']
    plays_player = ['X', 'Y', 'Z']
    total_score = 0
    for line in lines:
        strategies = line.split(' ')
        opponent = strategies[0]
        opponent_idx = plays_opponent.index(opponent)

        player = strategies[1]
        player_idx = plays_player.index(player)
        score = 0
        if player == 'X':
            score += ((opponent_idx - 1) %3) + 1
        elif player == 'Y':
            score = 3
            score += opponent_idx + 1
        elif player == 'Z':
            score = 6
            score += ((opponent_idx + 1) % 3) + 1
        total_score += score
    return total_score
            




def main(): 
    lines = get_lines()
    answer_part1 = part1(lines)
    print(answer_part1)
    answer_part2 = part2(lines)
    print(answer_part2)

if __name__ == "__main__": 
    main()