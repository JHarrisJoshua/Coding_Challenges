from collections import deque


def stackin_toys(on_santas_list):
    with open(on_santas_list, 'r') as santas_shop:
        in_stacks = []
        for toys in santas_shop:
            if '[' in toys:
                elves_stack(toys, in_stacks)
            if 'move' in toys:
                elves_shuffle(toys, in_stacks)
        top_shelf_toys = [toy_stack[-1] for toy_stack in in_stacks if toy_stack]
        return ''.join(top_shelf_toys)


def elves_stack(toys, in_toy_stacks):
    santa_r_us_aisle_num = 0
    for i, toy in enumerate(toys):
        if i % 4 == 1:
            santa_r_us_aisle_num += 1
            if len(in_toy_stacks) < santa_r_us_aisle_num:
                in_toy_stacks.append(deque([]))
            if toy.isalpha():
                in_toy_stacks[santa_r_us_aisle_num - 1].appendleft(toy)


def elves_shuffle(toys, in_stacks):
    move = [int(num) for num in toys.strip().split(' ') if num.isdigit()]
    for _ in range(move[0]):
        in_stacks[move[2] - 1].append(in_stacks[move[1] - 1].pop())


print(stackin_toys("AOC22_D05_inp.txt"))
