from math import inf


def main(file_name):
    with open(file_name, 'r') as infile:
        result, pos = 0, inf
        for line in infile:
            line = list(line.strip())
            for i, char in enumerate(line):
                if char == ')':
                    result -= 1
                elif char == '(':
                    result += 1
                if result < 0:
                    pos = min(pos, i+1)
    return result, pos


print(main("AOC15_D01_inp.txt"))
