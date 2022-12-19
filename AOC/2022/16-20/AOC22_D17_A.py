def elephant_tetris(file_name):
    with open(file_name, 'r') as infile:
        jets = list(infile.readline().strip())

    jet_num, rock_num = 0, 0
    while rock_num < 2022:
        rock = get_rock(rock_num % 5)
        jet_move(rock, jets[jet_num % len(jets)])


def jet_move(rock, jet):
    moves = {
        '>': (0,1),
        '<': (0,-1)
    }
    move = moves[jet]
    for row, col in rock:
        r, c = row + move[0], col + move[1]



def move():
    pass


def update_height():
    pass


def get_rock(num):
    rocks = {
        0: [(4,2),(4,3),(4,4),(4,5)],
        1: [(4,3),(6,3),(5,3),(5,2),(5,4)],
        2: [(4,2),(4,3),(4,4),(5,4),(6,4)],
        3: [(4,2),(5,2),(6,2),(7,2)],
        4: [(4,2),(5,2),(4,3),(5,3)]
    }
    return rocks[num]


print(elephant_tetris("AOC22_D17_inp0.txt"))
