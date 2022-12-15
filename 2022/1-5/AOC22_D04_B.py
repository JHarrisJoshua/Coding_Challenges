def duped_elves(file_name):
    santa_demerits = 0
    with open(file_name, 'r') as infile:
        for line in infile:
            line = [x.split('-') for x in line.strip().split(',')]
            merry_christmas = set(i for i in range(int(line[0][0]), int(line[0][1])+1))
            a_happy_new_year = set(i for i in range(int(line[1][0]), int(line[1][1])+1))
            if len(merry_christmas & a_happy_new_year) > 0:
                santa_demerits += 1
    return santa_demerits


print(duped_elves("AOC22_D04_inp.txt"))
