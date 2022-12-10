def lets_play_lite_brite(file_name):
    cycle, reg_val, result = 0, 1, 0
    grid = [['.' for _ in range(40)] for _ in range(6)]

    def push_some_pegs():
        row, col = divmod(cycle-1, 40)
        if col-1 <= reg_val <= col+1:
            grid[row][col] = 'X'

    with open(file_name, 'r') as infile:
        for line in infile:
            line = [(int(x) if (x.isdigit() or x[0] == '-') else x)
                    for x in line.strip().split(' ')]
            cycle += 1
            push_some_pegs()
            if line[0] == 'addx':
                cycle += 1
                push_some_pegs()
                reg_val += line[1]
    return grid


lite_brite_art = lets_play_lite_brite("AOC22_D10_inp.txt")
for grid_row in lite_brite_art:
    print(''.join(grid_row))
