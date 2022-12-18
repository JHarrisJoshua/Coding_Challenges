def main(file_name):
    houses, start = set(), (0,0)
    houses.add((start))
    moves = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0)
    }

    with open(file_name, 'r') as infile:
        row, col = start
        for line in infile:
            for i, char in enumerate(line):
                if char in moves:
                    dy, dx = moves[char]
                    row, col = row + dy, col + dx
                    houses.add((row, col))

    return len(houses)

print(main("AOC15_D03_inp.txt"))
