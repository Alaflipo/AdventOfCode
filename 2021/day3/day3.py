def get_lines():

    with open('2021/day3/input.txt') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def part1(lines):
    amount_lines = len(lines)
    positive_amounts = [0] * len(lines[0])
    for line in lines:
        for i, bit in enumerate(line):
            if (bit == '1'):
                positive_amounts[i] += 1

    gamma_rate_bin = ''
    epsilon_rate_bin = ''
    for score in positive_amounts:
        if (score > amount_lines/2):
            gamma_rate_bin += '1'
            epsilon_rate_bin += '0'
        else:
            gamma_rate_bin += '0'
            epsilon_rate_bin += '1'
    gamma_rate = int(gamma_rate_bin, 2)
    epsilon_rate = int(epsilon_rate_bin, 2)
    return gamma_rate * epsilon_rate


def part2(lines):
    amount_lines = len(lines)

    rates = [0, 0]
    for is_epsilon in range(2):
        power_codes = lines
        # For the gamma rate
        for bit_index in range(len(lines[0])):
            if len(power_codes) <= 1:
                break

            partition_1 = []
            partition_2 = []
            for line in power_codes:
                if (line[bit_index] == '1'):
                    partition_1.append(line)
                else:
                    partition_2.append(line)

            if not is_epsilon:
                power_codes = partition_1 if len(
                    partition_1) >= len(partition_2) else partition_2
            else:
                power_codes = partition_2 if len(
                    partition_1) >= len(partition_2) else partition_1

        rates[is_epsilon] = int(power_codes[0], 2)

    return rates[0] * rates[1]


def main():
    lines = get_lines()
    score = part1(lines)
    print(score)
    score = part2(lines)
    print(score)


if __name__ == '__main__':
    main()
