class Grid:
    def __init__(self):
        self.jet_num = 0
        self.rock_num = 0
        self.height = 0
        self.rocks = {(0,i) for i in range(7)}

    def elephant_tetris(self, file_name, simulation_size):
        with open(file_name, 'r') as infile:
            jets = list(infile.readline().strip())

        while self.rock_num < simulation_size:
            rock = get_rock(rock_num % 5, height)

            move_rock = True
            while move_rock:
                rock = jet_move(rocks, rock, jets[jet_num % len(jets)])[0]
                jet_num += 1
                rock, move_rock = jet_move(rocks, rock, 'down')
                # print_rock(rocks, height, rock)

            for row, col in rock:
                rocks.add((row, col))
                height = max(height, row)
            # print_rocks(rocks, height)
            rock_num += 1
            if rock_num % simulation_size/10000 == 0:
                print(rock_num, rock_num/simulation_size*100)
            if rock_num > 0 and rock_num % 100000 == 0:
                print(rock_num, rock_num / simulation_size * 100)

        return height

    def jet_move(self, rocks, rock, jet):
        moves = {
            '>': (0,1),
            '<': (0,-1),
            'down': (-1,0)
        }
        move = moves[jet]
        new_rock = []
        for row, col in rock:
            r, c = row + move[0], col + move[1]
            if not 0<=c<7 or r==0 or (r,c) in rocks:
                return rock, False
            new_rock.append((r,c))
        return new_rock, True

    def get_rock(self, num, height):
        rocks = {
            0: [(4,2),(4,3),(4,4),(4,5)],
            1: [(4,3),(6,3),(5,3),(5,2),(5,4)],
            2: [(4,2),(4,3),(4,4),(5,4),(6,4)],
            3: [(4,2),(5,2),(6,2),(7,2)],
            4: [(4,2),(5,2),(4,3),(5,3)]
        }
        rock = rocks[num]
        for i, (row, col) in enumerate(rock):
            rock[i] = (row + height, col)
        return rock

    def print_rocks(self, rocks, height):
        print("\n________________\n")
        for i in range(height+4, -1,-1):
            line = ''
            for j in range(7):
                line = line + 'X' if (i,j) in rocks else line + '0'
            print(line)
        print("\n________________\n")

    def print_rock(self, rocks, height, rock):
        print("\n________________\n")
        for i in range(height+4, -1,-1):
            line = ''
            for j in range(7):
                if (i,j) in rocks:
                    line += 'X'
                elif (i,j) in rock:
                    line += '@'
                else:
                    line += '0'
            print(line)
        print("________________")


simulation = Grid()
print(simulation.elephant_tetris("AOC22_D17_inp.txt", 2022))
