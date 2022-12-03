from collections import Counter
def total_sum():
    result = 0
    with open("AOC22_D03_inp.txt", 'r') as infile:
        for line in infile:
            line = line.strip().replace(' ', '')
            comp_len = int(len(line)/2)
            first, second = set(line[:comp_len]), set(line[comp_len:])
            common = ''.join(first & second)
            result += ord(common.lower()) - ord('a') + 1 + 26*(common.isupper())
    return result


print(total_sum())
