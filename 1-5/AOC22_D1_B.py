def max_food():
    with open("AOC22_D1_inp.txt", 'r') as infile:
        run_sum, hangry_elves = 0, []
        for line in infile:
            if len((clean_line := line.strip())) == 0:
                top_three(hangry_elves, run_sum)
                run_sum = 0
            else:
                run_sum += int(clean_line)
    return sum(hangry_elves)


def top_three(big_boys, contender):
    if len(big_boys) < 3:
        big_boys.append(contender)
    else:
        if contender > big_boys[-1]:
            big_boys[-1] = contender
        else:
            return  # from whence you came, little elf
    big_boys.sort(reverse=True)


print(max_food())
