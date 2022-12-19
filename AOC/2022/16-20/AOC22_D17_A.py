from collections import defaultdict
def elephant_tetris(file_name, simulation_size):
    with open(file_name, 'r') as infile:
        jets = list(infile.readline().strip())
    # print(jets, len(jets))
    print(len(jets))

    jet_num, rock_num, height = 0, 0, 0
    rocks = {(0,i) for i in range(7)}
    result = defaultdict(dict)

    while rock_num < simulation_size:
        rock = get_rock(rock_num % 5, height)

        move_rock = True
        while move_rock:
            rock = jet_move(rocks, rock, jets[jet_num % len(jets)])[0]
            jet_num += 1
            # if jet_num > 0 and jet_num % len(jets) == 0:
            #     print_rocks(rocks, height, rock_num)
            rock, move_rock = jet_move(rocks, rock, 'down')
            # if rock_num > 0 and rock_num % 20 == 0:
            #     print_rock(rocks, height, rock)

        for row, col in rock:
            rocks.add((row, col))
            height = max(height, row)
        # if rock_num > 0 and rock_num % 100 == 0:
        #     print_rocks(rocks, height)
        # if jet_num > 0 and jet_num % len(jets) == 0:
        #     print_rocks(rocks, height, rock_num)
        rock_num += 1
        # if jet_num > 0 and jet_num % len(jets) == 0:
        #     print_rocks(rocks, height)
        # if rock_num % simulation_size/10000 == 0:
        #     print(rock_num, rock_num/simulation_size*100)
        # if rock_num > 0 and rock_num % 100000 == 0:
        #     print(rock_num, rock_num / simulation_size * 100)
        # if rock_num > 0 and rock_num % 100000 == 0:
        #     print(rock_num, rock_num / simulation_size * 100)
        if rock_num in [5, 1715, 3425, 5135, 6220]:
            result[rock_num] = height
    return result


def jet_move(rocks, rock, jet):
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


def get_rock(num, height):
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


def print_rocks(rocks, height, rock_num):
    print("height", height, "rock num", rock_num)
    print("\n________________\n")
    for i in range(height+4, max(-1, height-100),-1):
        line = ''
        for j in range(7):
            line = line + 'X' if (i,j) in rocks else line + '0'
        print(line)
    print("\n________________\n")


def print_rock(rocks, height, rock):
    print("height", height)
    print("________________\n")
    for i in range(height+4, max(-1, height-100),-1):
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


heights = elephant_tetris("AOC22_D17_inp.txt", 6220)
print(heights)

height = 0
total_rocks = 1000000000000
total_rocks -= 6220
height += heights[6220]
print(total_rocks, height)
div, mod = divmod(total_rocks, 1710)
print(div, mod)
height += (heights[5135] - heights[3425]) * div
total_rocks -= (1710 * div)
print(total_rocks)
print(height)

# print("Rocks: 5", "Height: ", height_1)
# print("Rocks: 1715", "Height: ", height_2)
# print('change in rocks: ', 1715-5,'change in H: ', height_2 - height_1)
# print("Rocks: 3425", "Height: ", height_3)
# print('change in rocks: ', 3425-1715,'change in H: ', height_3 - height_2)

