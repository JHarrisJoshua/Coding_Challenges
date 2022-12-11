from collections import deque, Counter
import re


class MonkeyInTheMiddle:
    def __init__(self, file_name, rounds, monkeys_im_gonna_chase):
        self.monkeys_to_chase = monkeys_im_gonna_chase
        self.items = deque([])
        self.operations = {}
        self.tests = {}
        self.inspections = Counter()
        self.load_monkey_matrix_construct(file_name)
        self.stolen_item_tracker(rounds)


    def stolen_item_tracker(self, rounds):
        while self.items:
            round_n, monkey, worry_lvl = self.items.popleft()
            self.inspections[monkey] += 1
            worry_lvl = self.new_worry_level(monkey, worry_lvl)
            new_monkey = self.new_monkey(monkey, worry_lvl)
            if new_monkey > monkey:
                self.items.append((round_n, new_monkey, worry_lvl))
            elif round_n < rounds:
                self.items.append((round_n+1, new_monkey, worry_lvl))

    def new_monkey(self, monkey, worry):
        div, this_monkey, the_other_monkey = self.tests[monkey]
        return this_monkey if worry % div == 0 else the_other_monkey

    def new_worry_level(self, monkey, old):
        op, factor = self.operations[monkey]
        factor = old if factor == 'old' else factor
        new_level = (old+factor if op == '+' else old*factor) // 3
        return new_level

    def get_monkey_business_level(self):
        top_n = self.inspections.most_common(self.monkeys_to_chase)
        result = 1
        for monkey, level in top_n:
            result *= level
        return result

    def load_monkey_matrix_construct(self, file_name):
        with open(file_name, 'r') as infile:
            monkey = -1
            for i, line in enumerate(infile):
                line: str|list = line.strip()
                if line == '':
                    continue
                elif line[0] == 'M':
                    monkey += 1
                    self.inspections[monkey] = 0
                elif line[0] == 'S':
                    line = [int(x) for x in re.sub("[\sa-zA-Z:]+", '', line).split(',')]
                    [self.items.append((1, monkey, x)) for x in line]
                elif line[0] == 'O':
                    line = line.split(' ')
                    line[-1] = int(line[-1]) if line[-1].isdigit() else line[-1]
                    self.operations[monkey] = [line[-2], line[-1]]
                elif line[0] == 'T':
                    self.tests[monkey] = [int(re.sub("[\sa-zA-Z:]+", '', line))]
                elif line[0] == 'I':
                    self.tests[monkey].append(int(re.sub("[\sa-zA-Z:]+", '', line)))


if __name__ == '__main__':
    monkey_business = MonkeyInTheMiddle("AOC22_D11_inp.txt", 20, 2)
    print("items: ", monkey_business.items)
    print("inspections: ", monkey_business.inspections)
    print("operations: ", monkey_business.operations)
    print("tests: ", monkey_business.tests)

    print(monkey_business.get_monkey_business_level())




