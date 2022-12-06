import copy


def get_stacks():
    with open('2022/day5/input_stacks.txt') as f:
        lines = f.readlines()
        stacks = [[] for y in range(9)]

        for i in range(len(lines) - 1, -1, -1):
            characters = lines[i].split(' ')
            empty_count = 0
            stack_count = 0
            for i, character_string in enumerate(characters):
                if (character_string == ''):
                    empty_count += 1
                else:
                    stack_count += int(empty_count/4)
                    empty_count = 0
                    character = character_string.split('[')[1].split(']')[0]
                    stacks[stack_count].append(character)
                    stack_count += 1

        return stacks


def get_moves():
    moves = []
    with open('2022/day5/input_moves.txt') as f:
        lines = f.readlines()
        for line in lines:
            line_array = line.split(' ')
            moves.append([int(line_array[1]), int(
                line_array[3]), int(line_array[5].strip())])
    return moves


def part1(stacks, moves):
    for move in moves:
        amount = move[0]
        start_stack = move[1] - 1
        end_stack = move[2] - 1

        # get the crates
        crates = stacks[start_stack][-amount:]
        # because it is done one by one we reverse the list
        crates.reverse()
        # del the crates from the start stack
        del stacks[start_stack][-amount:]
        # append them to the end stack
        stacks[end_stack] = stacks[end_stack] + crates

    top_crates = [stack[-1] for stack in stacks]
    return ''.join(top_crates)


def part2(stacks, moves):
    for move in moves:
        amount = move[0]
        start_stack = move[1] - 1
        end_stack = move[2] - 1

        # get the crates
        crates = stacks[start_stack][-amount:]
        # del the crates from the start stack
        del stacks[start_stack][-amount:]
        # append them to the end stack
        stacks[end_stack] = stacks[end_stack] + crates

    top_crates = [stack[-1] for stack in stacks]
    return ''.join(top_crates)


def main():
    stacks = get_stacks()
    moves = get_moves()
    top_crates = part1(copy.deepcopy(stacks), moves)
    print(top_crates)
    top_crates = part2(copy.deepcopy(stacks), moves)
    print(top_crates)


if __name__ == '__main__':
    main()
