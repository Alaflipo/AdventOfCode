from __future__ import annotations
import time 
from dataclasses import dataclass

class Hand(): 

    hand_value_map = {"Five OAK": 7, "Four OAK": 6, "Full House": 5, "Three OAK": 4, "Two Pair": 3, "One Pair": 2, "High Card": 1}
    card_value_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


    def __init__(self, hand: str, bid: int, hand_type: str = "", hand_value=0, cards: dict = {}):
        self.hand = hand 
        self.bid = bid
        self.hand_type = hand_type
        self.hand_value = hand_value
        self.cards = cards

    def determine_hand_type(self): 
        self.cards = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0}
        for card in self.hand: 
            self.cards[card] += 1
        card_count = []
        for card in self.cards: 
            if (self.cards[card] > 0): card_count.append(self.cards[card])
        if 5 in card_count: self.hand_type = "Five OAK"
        elif 4 in card_count: self.hand_type = "Four OAK"
        elif 3 in card_count: 
            if 2 in card_count: self.hand_type = "Full House"
            else: self.hand_type = "Three OAK"
        elif card_count.count(2) == 2: self.hand_type = "Two Pair"
        elif 2 in card_count: self.hand_type = "One Pair"
        else: self.hand_type = "High Card"
        self.hand_value = self.hand_value_map[self.hand_type]
    
    def __lt__(self, other: Hand):
        if (self.hand_value == other.hand_value): 
            for i, card in enumerate(self.hand): 
                if (card != other.hand[i]): 
                    return self.card_value_map[card] < self.card_value_map[other.hand[i]]
        else: 
            return self.hand_value < other.hand_value
        
class HandJoker(): 

    hand_value_map = {"Five OAK": 7, "Four OAK": 6, "Full House": 5, "Three OAK": 4, "Two Pair": 3, "One Pair": 2, "High Card": 1}
    card_value_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


    def __init__(self, hand: str, bid: int, hand_type: str = "", hand_value=0, cards: dict = {}):
        self.hand = hand 
        self.bid = bid
        self.hand_type = hand_type
        self.hand_value = hand_value
        self.cards = cards

    def determine_hand_type(self): 
        self.cards = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0}
        for card in self.hand: 
            self.cards[card] += 1
        card_count = []
        for card in self.cards: 
            if card != 'J' and (self.cards[card] > 0): card_count.append(self.cards[card])
        if self.cards['J'] == 5: self.hand_type = "Five OAK"
        elif (5 - self.cards['J']) in card_count: self.hand_type = "Five OAK"
        elif (4 - self.cards['J']) in card_count: self.hand_type = "Four OAK"
        elif 3 in card_count: 
            if 2 in card_count: self.hand_type = "Full House"
            else: self.hand_type = "Three OAK"
        elif (3 - self.cards['J']) in card_count: 
            if card_count.count(2) == 2: self.hand_type = "Full House"
            else: self.hand_type = "Three OAK"
        elif card_count.count(2) == 2: self.hand_type = "Two Pair"
        elif (2 - self.cards['J']) in card_count: self.hand_type = "One Pair"
        else: self.hand_type = "High Card"
        
        self.hand_value = self.hand_value_map[self.hand_type]
    
    def __lt__(self, other: Hand):
        if (self.hand_value == other.hand_value): 
            for i, card in enumerate(self.hand): 
                if (card != other.hand[i]): 
                    return self.card_value_map[card] < self.card_value_map[other.hand[i]]
        else: 
            return self.hand_value < other.hand_value

def process_input_normal(lines): 
    hands = []
    for line in lines: 
        game = line.strip().split(" ")
        hand = Hand(hand=game[0], bid=int(game[1]))
        hand.determine_hand_type()
        hands.append(hand) 
    hands.sort()
    return hands

def process_input_joker(lines): 
    hands = []
    for line in lines: 
        game = line.strip().split(" ")
        hand = HandJoker(hand=game[0], bid=int(game[1]))
        hand.determine_hand_type()
        hands.append(hand) 
    hands.sort()
    return hands

def get_input(): 
    with open('./2023/day7/input.txt') as f: 
        lines = f.readlines()
        return lines 
    
def calculate_game_value(hands): 
    sum = 0 
    for i, hand in enumerate(hands): 
        sum += (hand.bid * (i + 1))
    return sum 
        
def part1(input):
    hands = process_input_normal(input)
    return calculate_game_value(hands)

def part2(input): 
    hands = process_input_joker(input)
    return calculate_game_value(hands)

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
