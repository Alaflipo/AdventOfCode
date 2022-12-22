import math
grid_size = 1000


def get_moves():
    with open('2022/day9/input.txt') as file:
        lines = file.readlines()
        moves = []
        for line in lines:
            moves.append(line.strip().split())
        return moves


def part1(moves):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    start_pos = int(grid_size/2)
    grid[start_pos][start_pos] = 1
    head_pos = [start_pos, start_pos]
    tail_pos = [start_pos, start_pos]
    for move in moves:
        direction = move[0]
        amount = int(move[1])
        for i in range(amount):
            # move head
            if direction == 'R':
                head_pos[1] += 1
            elif direction == 'L':
                head_pos[1] -= 1
            elif direction == 'U':
                head_pos[0] -= 1
            elif direction == 'D':
                head_pos[0] += 1

            # move tail
            if (abs(tail_pos[0] - head_pos[0]) > 1 or abs(tail_pos[1] - head_pos[1]) > 1):
                x_dir = head_pos[0] - tail_pos[0]
                y_dir = head_pos[1] - tail_pos[1]
                if (abs(x_dir) > 0 and abs(y_dir) > 0):
                    tail_pos[0] += int(math.copysign(1, x_dir))
                    tail_pos[1] += int(math.copysign(1, y_dir))
                elif (abs(x_dir) > 0):
                    tail_pos[0] += int(math.copysign(1, x_dir))
                elif (abs(y_dir) > 0):
                    tail_pos[1] += int(math.copysign(1, y_dir))

                # update grid
                grid[tail_pos[0]][tail_pos[1]] = 1
    path = 0
    for row in grid:
        path += sum(row)
    return path


def part2(moves):
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    start_pos = int(grid_size/2)
    grid[start_pos][start_pos] = 1
    rope_pos = [[start_pos, start_pos] for _ in range(10)]
    for move in moves:
        direction = move[0]
        amount = int(move[1])
        for i in range(amount):
            # move head
            if direction == 'R':
                rope_pos[0][1] += 1
            elif direction == 'L':
                rope_pos[0][1] -= 1
            elif direction == 'U':
                rope_pos[0][0] -= 1
            elif direction == 'D':
                rope_pos[0][0] += 1

            for i, current_knot in enumerate(rope_pos[1:]):
                previous_knot = rope_pos[i]
                # move tail
                if (abs(current_knot[0] - previous_knot[0]) > 1 or abs(current_knot[1] - previous_knot[1]) > 1):
                    x_dir = previous_knot[0] - current_knot[0]
                    y_dir = previous_knot[1] - current_knot[1]
                    if (abs(x_dir) > 0 and abs(y_dir) > 0):
                        current_knot[0] += int(math.copysign(1, x_dir))
                        current_knot[1] += int(math.copysign(1, y_dir))
                    elif (abs(x_dir) > 0):
                        current_knot[0] += int(math.copysign(1, x_dir))
                    elif (abs(y_dir) > 0):
                        current_knot[1] += int(math.copysign(1, y_dir))

                    # update grid
                    if (i == len(rope_pos) - 2):
                        grid[current_knot[0]][current_knot[1]] = 1
    path = 0
    for row in grid:
        path += sum(row)
    return path


def main():
    moves = get_moves()
    cells_visited = part1(moves)
    print(cells_visited)
    cells_visited = part2(moves)
    print(cells_visited)


if __name__ == "__main__":
    main()
