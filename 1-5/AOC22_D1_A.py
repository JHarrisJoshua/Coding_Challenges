def max_food():
    with open("AOC22_D1_inp.txt", 'r') as infile:
        max_sum, run_sum = 0, 0
        for line in infile:
            if len((nice_line := line.strip())) == 0:
                max_sum, run_sum = max(max_sum, run_sum), 0
            else:
                run_sum += int(nice_line)
    return max_sum


print(max_food())
