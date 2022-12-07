
def get_positions():
    with open('2021/day7/input.txt') as file:
        input_array = file.readline().strip().split(',')
        return [int(position) for position in input_array]


def part1(positions):
    highest_pos = max(positions)
    costs = []
    for mark in range(highest_pos + 1):
        cost = 0
        for pos in positions:
            cost += abs(pos-mark)
        costs.append(cost)
    return min(costs)


def part2(positions):
    highest_pos = max(positions)
    costs = []
    for mark in range(highest_pos + 1):
        cost = 0
        for pos in positions:
            # sum factorial
            n = abs(pos-mark)
            cost += int((n**2 + n) / 2)
        costs.append(cost)
    return min(costs)


def main():
    positions = get_positions()
    lowest_cost = part1(positions=positions)
    print(lowest_cost)
    lowest_cost = part2(positions=positions)
    print(lowest_cost)


if __name__ == "__main__":
    main()
