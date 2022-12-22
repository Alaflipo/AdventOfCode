
def get_monkeys():
    with open('2022/day11/input.txt') as file:
        lines = file.readlines()
        monkeys = []
        for m in range(int((len(lines) + 1) / 7)):
            monkey = {
                'items': [],
                'operation': 0,
                'test': '',
                'decision': [0, 0]
            }
            start = m * 7
            # Starting items of each monkey
            starting_items = lines[start + 1].strip().split(': ')[1].split(',')
            monkey['items'] = [int(item.strip()) for item in starting_items]
            # Operation of each monekey
            monkey['operation'] = lines[start + 2].strip().split('= ')[1]
            # Divisible test
            monkey['test'] = int(lines[start + 3].strip().split('by ')[1])
            # If true ... if False ...
            monkey['decision'][0] = int(lines[start +
                                              4].strip().split('monkey ')[1])
            monkey['decision'][1] = int(lines[start +
                                              5].strip().split('monkey ')[1])
            monkeys.append(monkey)
        return monkeys


def part1(monkeys):
    items_inspected = [0 for _ in range(len(monkeys))]
    for round in range(20):
        for m, monkey in enumerate(monkeys):
            items_inspected[m] += len(monkey['items'])
            for item in monkey['items']:
                old = item
                new_value = int(eval(monkey['operation']) / 3)
                if (new_value % monkey['test'] == 0):
                    monkeys[monkey['decision'][0]]['items'].append(new_value)
                else:
                    monkeys[monkey['decision'][1]]['items'].append(new_value)
            monkey['items'] = []
    items_inspected.sort(reverse=True)
    return items_inspected[0] * items_inspected[1]


def part2(monkeys):
    modulo = 1
    for monkey in monkeys:
        # to make code more efficient we're gonna work in modular arithmetic
        modulo *= monkey['test']
    items_inspected = [0 for _ in range(len(monkeys))]
    for round in range(10000):
        for m, monkey in enumerate(monkeys):
            items_inspected[m] += len(monkey['items'])
            for item in monkey['items']:
                old = item
                new_value = int(eval(monkey['operation'])) % modulo // 1
                if (new_value % monkey['test'] == 0):
                    monkeys[monkey['decision'][0]]['items'].append(new_value)
                else:
                    monkeys[monkey['decision'][1]]['items'].append(new_value)
            monkey['items'] = []
    items_inspected.sort(reverse=True)
    return items_inspected[0] * items_inspected[1]


def main():
    monkeys = get_monkeys()
    monkey_business = part1(monkeys)
    print(monkey_business)
    monkey_business = part2(monkeys)
    print(monkey_business)


if __name__ == '__main__':
    main()
