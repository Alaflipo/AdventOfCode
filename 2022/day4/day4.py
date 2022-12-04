def get_lines():
    ranges = []

    with open('2022/day4/input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
            elves = lines[i].split(',')
            startids = []
            endids = []

            for elf in elves:
                elfinfo = elf.split('-')
                startids.append(int(elfinfo[0]))
                endids.append(int(elfinfo[1]))

            ranges.append([startids, endids])

    return ranges


def part1(ranges):
    double = 0
    for range in ranges:
        if range[0][0] >= range[0][1] and range[1][0] <= range[1][1] or \
           range[0][0] <= range[0][1] and range[1][0] >= range[1][1]:
            double += 1

    return double


def part2(ranges):
    double = 0
    for range in ranges:
        startids = range[0]
        endids = range[1]

        if startids[0] >= startids[1] and startids[0] <= endids[1]:
            double += 1
        elif endids[0] >= startids[1] and endids[0] <= endids[1]:
            double += 1
        elif startids[1] >= startids[0] and startids[1] <= endids[0]:
            double += 1
        elif endids[1] >= startids[0] and endids[1] <= endids[0]:
            double += 1

    return double


def main():
    ranges = get_lines()
    answer_part1 = part1(ranges)
    print(answer_part1)
    answer_part2 = part2(ranges)
    print(answer_part2)


if __name__ == "__main__":
    main()
