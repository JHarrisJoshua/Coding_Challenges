def total_score() -> int:
    guide = {'A':1, 'B':2, 'C':3,'X':1, 'Y':0, 'Z':2}
    outcome = [3, 0, 6]  # 0-Draw(Y), 1-Lost(X), 2-Win(Z)
    result = 0

    with open("AOC22_D2_inp.txt", 'r') as infile:
        for line in infile:
            line = line.strip()
            # Normalize game to 0-Draw, 1-Lost, 2-Win
            elf1, game = guide[line[0]], guide[line[2]]
            # Back out Elf2 using Game and Elf1
            elf2 = elf1 - game + 3 * (game >= elf1)
            score = elf2 + outcome[game]
            result += score
    return result


print(total_score())
