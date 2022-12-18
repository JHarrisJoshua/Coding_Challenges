def duped_elves(file_name):
    santa_demerits = 0
    with open(file_name, 'r') as infile:
        for line in infile:
            line = [list(map(int, x.split('-'))) for x in line.strip().split(',')]
            elf, on, a, shelf = line[0][0], line[0][1], line[1][0], line[1][1]
            if (elf <= a and on >= shelf) or (elf >= a and on <= shelf):
                santa_demerits += 1
    return santa_demerits


print(duped_elves("AOC22_D04_inp.txt"))
