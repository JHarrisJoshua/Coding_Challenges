def main(file_name):
    with open(file_name, 'r') as infile:
        for line in infile:
            line = list(line.strip().replace(' ', ''))
            print(line)

print(main("AOC22_D14_inp.txt"))
