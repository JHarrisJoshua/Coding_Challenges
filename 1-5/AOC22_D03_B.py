def total_sum():
    result = 0
    with open("AOC22_D03_inp.txt", 'r') as infile:
        for i, line in enumerate(infile):
            line = line.strip().replace(' ', '')
            if i % 3 == 0:
                common = set(line)
            else:
                common = common & set(line)

            if i % 3 == 2:
                common = ''.join(common)
                result += ord(common.lower()) - ord('a') + 1 + 26*(common.isupper())
    return result


print(total_sum())
