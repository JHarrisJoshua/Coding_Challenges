def total_score():
    choice = {'A':1, 'B':2, 'C':3,'X':1, 'Y':2, 'Z':3}
    outcome = [3, 0, 6]  # 0-Draw, 1-Lost, 2-Win
    result = 0

    with open("AOC22_D02_inp.txt", 'r') as infile:
        for line in infile:
            line = line.strip()
            elf1, elf2 = choice[line[0]], choice[line[2]]
            # Normalize game to 0-Draw, 1-Lost, 2-Win
            game = elf1 - elf2 + 3 * (elf2 > elf1)
            score = elf2 + outcome[game]
            result += score
    return result


print(total_score())
