import time 

def get_input(): 
    with open('./2019/day3/input.txt') as f: 
        wires = [instructions.strip().split(',') for instructions in f.readlines()]
        return wires

def set_board(board, player, dist, head, value): 
    crossings = []
    for _ in range(dist): 
        head[0] += value[0]
        head[1] += value[1]
        if board[head[1]][head[0]] == 'o': 
            crossings.append(head.copy())
        board[head[1]][head[0]] = player
    return crossings
        
    
def part1(input):
    board = [[' '] * 20000 for _ in range(20000)]
    start = [10000, 10000]
    players = ['o', '+']
    intersects = []
    for i, wire in enumerate(input): 
        head = start.copy()
        for inst in wire: 
            direction = inst[0]
            dist = int(inst[1:])
            crossings = []
            match direction: 
                case 'R':
                    crossings = set_board(board, players[i], dist, head, [1, 0])
                case 'L':
                    crossings = set_board(board, players[i], dist, head, [-1, 0])
                case 'U':
                    crossings = set_board(board, players[i], dist, head, [0, 1])
                case 'D':
                    crossings = set_board(board, players[i], dist, head, [0, -1])
            for c in crossings: intersects.append(c)
    distances = []
    for cross in intersects: 
        distances.append(abs(start[0] - cross[0]) + abs(start[1] - cross[1]))
    return min(distances)



def set_board_2(boards, player, counter, dist, head, value): 
    crossings = []
    for _ in range(dist): 
        head[0] += value[0]
        head[1] += value[1]
        if boards[player][head[1]][head[0]] < 0: 
            boards[player][head[1]][head[0]] = counter 
        if player == 1 and boards[0][head[1]][head[0]] > 0: 
            crossings.append([boards[0][head[1]][head[0]], counter])
        counter += 1
    return crossings, counter
    
def part2(input): 
    board1 = [[-1] * 20000 for _ in range(20000)]
    board2 = [[-1] * 20000 for _ in range(20000)]
    boards = [board1, board2]
    start = [10000, 10000]
    intersects = []
    for player, wire in enumerate(input): 
        counter = 1
        head = start.copy()
        for inst in wire: 
            direction = inst[0]
            dist = int(inst[1:])
            crossings = []
            match direction: 
                case 'R':
                    crossings, counter = set_board_2(boards, player, counter, dist, head, [1, 0])
                case 'L':
                    crossings, counter = set_board_2(boards, player, counter, dist, head, [-1, 0])
                case 'U':
                    crossings, counter = set_board_2(boards, player, counter, dist, head, [0, 1])
                case 'D':
                    crossings, counter = set_board_2(boards, player, counter, dist, head, [0, -1])
            for c in crossings: intersects.append(c)
    distances = []
    for cross in intersects: 
        distances.append(cross[0] + cross[1])
    return min(distances)

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
