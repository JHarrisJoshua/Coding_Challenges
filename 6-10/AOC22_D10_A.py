def signal_strength(file_name):
    cycle, cycles, reg_val, result = 0, {}, 1, 0

    def sum_result(total=0):
        if any([cycle == 20, ((cycle - 20) % 40) == 0]):
            cycles[cycle] = reg_val
            total += cycle * reg_val
        return total

    with open(file_name, 'r') as infile:
        for line in infile:
            line = [(int(x) if (x.isdigit() or x[0] == '-') else x)
                    for x in line.strip().split(' ')]
            cycle += 1
            result += sum_result()
            if line[0] == 'addx':
                cycle += 1
                result += sum_result()
                reg_val += line[1]
            if len(cycles) == 6:
                return result


print(signal_strength("AOC22_D10_inp.txt"))
