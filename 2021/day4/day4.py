
def get_numbers():
    with open('2021/day4/tombola.txt') as f:
        output = f.readline()
        return [int(number.strip()) for number in output.split(',')]


def get_boards():
    with open('2021/day4/boards.txt') as f:
        lines = f.readlines()
        line_counter = 0
        boards = []
        board = [[] for _ in range(5)]

        for line in lines:
            if (line == '\n'):
                boards.append(board)
                line_counter = 0
                board = [[] for _ in range(5)]
            else:
                numbers = line.split(' ')
                for number in numbers:
                    if (number != ''):
                        board[line_counter].append(int(number.strip()))
                line_counter += 1
        boards.append(board)
        return boards


def check_win(board, row_ball, column_ball):
    has_row = True
    has_column = True
    for number in board[row_ball]:
        if (number != None):
            has_row = False
            break
    for row in board:
        for column, number in enumerate(row):
            if (column == column_ball and number != None):
                has_column = False
                break
    return has_row or has_column


def play_game(boards, tombola):
    for ball in tombola:
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for c, number in enumerate(row):
                    if number == ball:
                        boards[b][r][c] = None
                        if check_win(board, r, c):
                            return board, ball
    return None


def get_board_score(winner):
    total = 0
    for row in winner:
        for number in row:
            if number != None:
                total += number
    return total


def part1(boards, tombola):
    winner, ball = play_game(boards, tombola)
    board_score = get_board_score(winner)
    return board_score * ball


def play_games_loser(boards, tombola):
    for ball in tombola:
        boards_to_delete = []
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for c, number in enumerate(row):
                    if number == ball:
                        boards[b][r][c] = None
                        if check_win(board, r, c):
                            if (len(boards) <= 1):
                                return board, ball
                            else:
                                boards_to_delete.append(board)
        for board in boards_to_delete:
            boards.remove(board)

    return None


def part2(boards, tombola):
    loser, ball = play_games_loser(boards, tombola)
    board_score = get_board_score(loser)
    return board_score * ball


def main():
    tombola = get_numbers()
    boards = get_boards()
    score = part1(boards, tombola)
    print(score)
    score = part2(boards, tombola)
    print(score)


if __name__ == "__main__":
    main()
