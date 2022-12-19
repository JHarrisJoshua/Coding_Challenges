def main(file_name):
    start = (0, 0)
    moves = {

    }
    with open(file_name, 'r') as infile:
        for line in infile:
            line = line.strip().split(', ')
            print(line)


print(main("AOC16_D01_inp0.txt"))
