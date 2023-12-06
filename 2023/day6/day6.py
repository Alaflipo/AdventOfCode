from __future__ import annotations
import time 
from dataclasses import dataclass

@dataclass 
class Game: 
    max_time: int 
    max_dist: int 
    wins: int = 0 

    def simulate_game(self, wait): 
        return ((self.max_time - wait) * wait) > self.max_dist

    def simulate_games(self): 
        for wait in range(self.max_time): 
            if (self.simulate_game(wait)): self.wins += 1
        return self.wins
    
def process_as_one_game(lines): 
    results = [] 
    for line in lines: 
        results.append(''.join([char for char in line if char.isnumeric()]))
    return Game(max_time=int(results[0]), max_dist=int(results[1]))

def process_as_multiple_games(lines): 
    time = [int(number) for number in lines[0].split(' ')[1:] if number != '']
    distance = [int(number) for number in lines[1].split(' ')[1:] if number != '']
    games = [Game(max_time=time[i], max_dist=distance[i]) for i in range(len(time))]
    return games

def get_input(): 
    with open('./2023/day6/input.txt') as f: 
        lines = [line.strip() for line in f.readlines()]
        return lines 
    
def part1(input):
    games = process_as_multiple_games(input)
    sum = 1 
    for game in games: 
        sum *= game.simulate_games()
    return sum

def part2(input): 
    game = process_as_one_game(input)
    return game.simulate_games()

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
