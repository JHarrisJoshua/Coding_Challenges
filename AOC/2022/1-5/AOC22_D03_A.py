def rucksack_sum(file_name):
    total = 0
    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip()
            split = len(line)//2
            first, second = set(line[:split]), set(line[split:])
            common = (first & second).pop()
            total += ord(common.lower()) - ord('a') + 26*(common.isupper()) + 1
    return total


print(rucksack_sum("AOC22_D03_inp.txt"))
