import copy


def get_input():
    with open('2021/day6/input.txt') as file:
        fishes = file.readline().split(',')
        return [int(fish.strip()) for fish in fishes]


def part1(fish):
    days = 0
    while days < 80:
        for fish_idx in range(len(fish) - 1, -1, -1):
            fish[fish_idx] -= 1
            if (fish[fish_idx] == -1):
                fish.append(8)
                fish[fish_idx] = 6
        days += 1
    return len(fish)


def part2(fish):
    days = 0
    groups = [0] * 9
    for f in fish:
        groups[f] += 1

    while days < 256:
        new_groups = [0] * 9
        for i, group in enumerate(groups):
            if (i == 0):
                new_groups[8] += group
                new_groups[6] += group
            else:
                new_groups[i-1] += group
        groups = new_groups
        days += 1
    return (sum(groups))


def main():
    fish = get_input()
    amount_fish = part1(copy.deepcopy(fish))
    print(amount_fish)
    amount_fish = part2(copy.deepcopy(fish))
    print(amount_fish)


if __name__ == "__main__":
    main()
