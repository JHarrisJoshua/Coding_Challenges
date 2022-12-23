from collections import deque
import re


def main(file_name):
    grove, cols, start = [], 0, None
    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip('\n')
            if 'L' in line:
                turns = list(re.sub(r"[0-9]+", '', line))
                steps = list(map(int,re.sub(r"[\sa-zA-Z:,;=]+",',', line).split(',')))
                print(steps, turns)
            elif len(line) > 0:
                grove.append(list(re.sub(r"\s", '0', line)))
                cols = max(cols, len(line))

    for i,row in enumerate(grove):
        if len(row) < cols:
            grove[i].extend(['0' for _ in range(cols - len(row))])
        if i==0:
            for j, val in enumerate(row):
                if val=='.':
                    start = (0, j)
                    break

    for i,row in enumerate(grove):
        print(row)

    print(start)

    turns, steps, facing = deque(turns), deque(steps), 0
    while turns:
        turn = turns.popleft()
        step = steps.popleft()


print(main("AOC22_D22_inp0.txt"))
