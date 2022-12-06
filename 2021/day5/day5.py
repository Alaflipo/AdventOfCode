
def get_coordinates():
    # returns [[x1, y1], [x2, y2]]
    with open('2021/day5/input.txt') as file:
        lines = file.readlines()
        coordinates = []
        for line in lines:
            path = line.strip().split(' -> ')
            path_array = []
            for coordinate in path:
                numbers = coordinate.split(',')
                path_array.append([int(numbers[0]), int(numbers[1])])
            coordinates.append(path_array)

        return coordinates


def get_score(plane):
    counter = 0
    for row in plane:
        for number in row:
            if number >= 2:
                counter += 1

    return counter


def part1(coordinates):
    plane = [[0] * 1000 for _ in range(1000)]
    for coordinate in coordinates:
        x1 = coordinate[0][0]
        y1 = coordinate[0][1]
        x2 = coordinate[1][0]
        y2 = coordinate[1][1]

        if (x1 == x2):
            for i in range(min(y1, y2), max(y1, y2) + 1):
                plane[i][x1] += 1
        if (y1 == y2):
            for i in range(min(x1, x2), max(x1, x2) + 1):
                plane[y1][i] += 1

    return get_score(plane)


def part2(coordinates):
    plane = [[0] * 1000 for _ in range(1000)]
    for coordinate in coordinates:
        x1 = coordinate[0][0]
        y1 = coordinate[0][1]
        x2 = coordinate[1][0]
        y2 = coordinate[1][1]

        if (x1 == x2):
            for i in range(min(y1, y2), max(y1, y2) + 1):
                plane[i][x1] += 1
        elif (y1 == y2):
            for i in range(min(x1, x2), max(x1, x2) + 1):
                plane[y1][i] += 1
        else:
            miny = min(coordinate, key=lambda c: c[1])
            maxy = max(coordinate, key=lambda c: c[1])
            difference = abs(x1 - x2)

            for i in range(difference + 1):
                if miny[0] < maxy[0]:
                    plane[miny[1] + i][miny[0] + i] += 1
                else:
                    plane[miny[1] + i][miny[0] - i] += 1

    return get_score(plane)


def main():
    coordinates = get_coordinates()
    amount_dangerous_spots = part1(coordinates=coordinates)
    print(amount_dangerous_spots)
    amount_dangerous_spots = part2(coordinates=coordinates)
    print(amount_dangerous_spots)


if __name__ == '__main__':
    main()
