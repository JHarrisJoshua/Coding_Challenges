from collections import deque


def main(file_name):
    with open(file_name, 'r') as infile:
        stacks = deque([])
        for line in infile:
            if '[' in line:
                line = line.replace('    ', '0')
                line = [char for char in line if char not in [' ', '[', ']', '\n']]
                if not stacks:
                    stacks = [deque([]) for _ in range(len(line))]
                for i, val in enumerate(line):
                    if len(stacks) == i:
                        stacks.append(deque([]))
                    if val != '0':
                        stacks[i].appendleft(val)
            if 'move' in line:
                move = [int(num) for num in line.strip().split(' ') if num.isdigit()]
                for i in range(move[0]):
                    if stacks[move[1] - 1]:
                        stacks[move[2] - 1].append(stacks[move[1] - 1].pop())

        result = [stack[-1] for stack in stacks if stack]

        return ''.join(result)


print(main("AOC22_D05_inp.txt"))
