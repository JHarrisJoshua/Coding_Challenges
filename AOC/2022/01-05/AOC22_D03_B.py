def rucksack_sum(file_name):
    total = 0
    with open(file_name, 'r') as infile:
        for i, line in enumerate(infile):
            line = set(line.strip())
            badge = line if i % 3 == 0 else badge.intersection(line)
            if i % 3 == 2:
                badge = badge.pop()
                total += ord(badge.lower()) - ord('a') + 26*badge.isupper() + 1
    return total


print(rucksack_sum("AOC22_D03_inp.txt"))
