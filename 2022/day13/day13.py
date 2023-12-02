
def get_input():
    with open('2022/day13/input.txt') as file:
        lines = file.readlines()
        packetpairs = []
        for i in range(0, len(lines) - 1, 3):
            packetpair = []
            packetpair.append(eval(lines[i]))
            packetpair.append(eval(lines[i+1]))
            packetpairs.append(packetpair)
        return packetpairs


def comparepairs(first_packet, second_packet):
    for idx, element_first in enumerate(first_packet):
        if (idx > len(second_packet) - 1):
            return False
        element_second = second_packet[idx]

        if type(element_first) == list:
            if type(element_second) == list:
                return comparepairs(element_first, element_second)
            else:
                return comparepairs(element_first, [element_second])
        else:
            if type(element_second) == list:
                return comparepairs([element_first], element_second)
            elif (element_first < element_second):
                return True
            elif (element_first > element_second):
                return False
    if len(first_packet) < len(second_packet):
        return True


def part1(packetpairs):
    sum_of_indices = 0
    for idx, pp in enumerate(packetpairs):
        sum_of_indices += (idx + 1) * comparepairs(pp[0], pp[1])
    return sum_of_indices


def main():
    packetpairs = get_input()
    sum_of_indices = part1(packetpairs)
    print(sum_of_indices)


if __name__ == "__main__":
    main()
