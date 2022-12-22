import copy


def get_map():
    with open('2022/day12/input.txt') as file:
        letter_map = [row.strip() for row in file.readlines()]
        int_map = [[0 for _ in letter_map[0]] for _ in letter_map]
        for y, row in enumerate(letter_map):
            for x, letter in enumerate(row):
                number = (ord(letter) - 97)
                if (number >= 0):
                    int_map[y][x] = number
                else:
                    int_map[y][x] = letter
        return int_map


# def search_best_path(map, path):
#     current_pos = path[-1]
#     current_height = map[current_pos[1]][current_pos[0]]
#     print(path)
#     if (current_height == 'E') or len(path) >= 5:
#         return len(path)

#     # previous_pos = path[-2]
#     # dif = [0, 0]
#     # for i in range(2):
#     #     dif[i] = current_pos[i] - previous_pos[i]

#     distances = []
#     directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     for direction in directions:
#         new_x = current_pos[0] + direction[0]
#         new_y = current_pos[1] + direction[1]
#         if (new_x < len(map[0]) and new_x >= 0 and new_y < len(map) and new_y >= 0 and current_height != 'S'):
#             new_height = map[new_x][new_y]
#             if (new_height == current_height + 1):
#                 path.append([new_x, new_y])
#                 distances.append(search_best_path(map, path))
#                 path.pop(-1)
#     return min(distances) if len(distances) > 0 else 10000


def bfs(map, options, visited):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    checked_map = copy.deepcopy(map)
    found_depth = 0

    while len(options) > 0:
        current_pos, depth = options.pop(0)
        current_height = map[current_pos[1]][current_pos[0]]
        for direction in directions:
            new_x = current_pos[0] + direction[0]
            new_y = current_pos[1] + direction[1]
            new_index = new_x + new_y * len(map[0])

            if (new_x < len(map[0]) and new_x >= 0 and new_y < len(map) and new_y >= 0 and new_index not in visited):
                new_height = map[new_y][new_x]

                if (new_height == 'E'):
                    if (current_height == 25):
                        found_depth = depth + 1
                elif (new_height <= current_height + 1):
                    options.append(([new_x, new_y], depth + 1))
                    visited.append(new_index)
                    checked_map[new_y][new_x] = 'x'

    return found_depth


def part1(map):
    coordinate = [0, 0]
    visited = []
    for j, row in enumerate(map):
        for i, height in enumerate(row):
            if (height == 'S'):
                map[j][i] = 0
                coordinate[0] = i
                coordinate[1] = j
                visited.append(j * len(map) + i)
                break
    options = [(coordinate, 0)]

    shortest_path = bfs(map, options, visited)
    return shortest_path


def part2(map):
    options = []
    visited = []
    for j, row in enumerate(map):
        for i, height in enumerate(row):
            if (height == 'S' or height == 0):
                map[j][i] = 0
                options.append(([i, j], 0))
                visited.append(j * len(map) + i)
                break

    shortest_path = bfs(map, options, visited)
    return shortest_path


def main():
    mountain_map = get_map()
    length_shortest_path = part1(mountain_map)
    print(length_shortest_path)
    length_hike_path = part2(mountain_map)
    print(length_hike_path)


if __name__ == "__main__":
    main()
