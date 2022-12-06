def get_input():
    with open('2022/day6/input.txt') as file:
        input = file.readline().strip()
        return input


def get_marker(buffer, indicator):
    string_marker = []
    for index, character in enumerate(buffer):
        string_marker += [character]

        if len(string_marker) > indicator:
            string_marker = string_marker[1:]
            if (len(set(string_marker)) == indicator):
                return index + 1


def main():
    buffer = get_input()
    packet_marker = get_marker(buffer, 4)
    print(packet_marker)
    message_marker = get_marker(buffer, 14)
    print(message_marker)


if __name__ == "__main__":
    main()
