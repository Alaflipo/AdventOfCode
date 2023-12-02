import time 

# [[[],[],[]]]

def get_input(): 
    with open('./2023/day2/input.txt') as f: 
        lines = f.readlines() 
        games = []
        for line in lines: 
            game = line.strip('\n')
            sets = game.split(":")[1].split(';')
            bag_draws = []
            for s in sets: 
                balls = s.split(',')
                ball_dict = {'red': 0, 'green': 0, 'blue': 0}
                for ball in balls: 
                    color = ball.strip().split(' ')
                    ball_dict[color[1]] = int(color[0])
                bag_draws.append(ball_dict)
            games.append(bag_draws)
        
        return games
    
def part1(input):
    colors = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0 
    for index, game in enumerate(input): 
        too_large = False 
        for draw in game: 
            for key in colors: 
                if draw[key] > colors[key]: 
                    too_large = True 
                    break 
            if too_large: 
                break 
        if not too_large: 
            sum += (index + 1)
        
    return sum


def part2(input): 
   
    sum = 0 
    for index, game in enumerate(input): 
        colors = {'red': 0, 'green': 0, 'blue': 0}
        too_large = False 
        for draw in game: 
            for key in colors: 
                if draw[key] > colors[key]: 
                    colors[key] = draw[key]
        sum += (colors['red'] * colors['green'] * colors['blue'])
        
    return sum

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
