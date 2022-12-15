from math import inf
from collections import deque


class Cave:
    def __init__(self):
        self.minimap = []
        self.sandy_source = (0, 500)
        self.count = 0

    def main(self, file_name):
        with open(file_name, 'r') as infile:
            slices = deque(infile.readlines())
            for i, line in enumerate(slices):
                slices[i] = [[int(num) for num in rock.split(sep=',')]
                             for rock in line.strip().split(sep=' -> ')]

        # print(slices)
        min_x, max_x, min_y, max_y = inf, -inf, 0, -inf
        for i, row in enumerate(slices):
            for j, rock in enumerate(row):
                x, y = rock
                min_x, max_x, min_y, max_y = (min(min_x, x), max(max_x, x),
                                              min(min_y, y), max(max_y, y))

        min_x, max_x, min_y, max_y = min_x-1, max_x+1, min_y, max_y+1
        boundaries = min_x, max_x, min_y, max_y
        rows, cols = max_y - min_y + 1, max_x - min_x + 1
        # print(min_x, max_x, min_y, max_y)
        # print(rows, cols)
        self.sandy_source = (self.sandy_source[0], self.sandy_source[1] - min_x)
        # print(self.sandy_source)
        self.make_cave(rows, cols, self.sandy_source)

        for i in range(len(slices)):
            rock_1, rock_2 = None, None
            for j, rock in enumerate(slices[i]):
                rock_2, rock_1 = rock, rock_2
                if rock_1 and rock_2:
                    self.map_cave(rock_1, rock_2, boundaries)
        fill_with_sand = True
        while fill_with_sand:
            fill_with_sand = self.fill_cave()
        return self.count

    def fill_cave(self):
        try:
            row, col = self.sandy_source[0], self.sandy_source[1]
            while row < (limit := len(self.minimap) - 2):
                while self.minimap[row+1][col] not in ['#','0'] and row<limit:
                    row, col = row+1, col
                if self.minimap[row+1][col-1] not in ['#','0']:
                    row, col = row + 1, col - 1
                elif self.minimap[row + 1][col + 1] not in ['#', '0']:
                    row, col = row + 1, col + 1
                elif self.minimap[row + 1][col] in ['#', '0']:
                    self.minimap[row][col] = '0'
                    self.count += 1
                    return True
            return False
        except:
            print(row, col)

    def map_cave(self, rock_1, rock_2, boundaries):
        min_x, max_x, min_y, max_y = boundaries
        move = (rock_2[0]-rock_1[0], rock_2[1]-rock_1[1])
        step = tuple(num//max(abs(move[0]), abs(move[1])) for num in move)
        # print('test')
        # print(rock_1, rock_2)
        # print(move, step)
        x_1, y_1 = rock_1[0]-min_x, rock_1[1]-min_y
        x_2, y_2 = rock_2[0]-min_x, rock_2[1]-min_y
        self.minimap[y_1][x_1] = self.minimap[y_2][x_2] = '#'
        while (x_1, y_1) != (x_2, y_2):
            x_1, y_1 = x_1 + step[0], y_1 + step[1]
            self.minimap[y_1][x_1] = '#'


    def make_cave(self, rows, cols, start):
        self.minimap = [['~' for _ in range(cols)] for _ in range(rows)]
        self.minimap[start[0]][start[1]] = '+'


cave = Cave()
print("Part 1:  ", cave.main("AOC22_D14_inp.txt"))
cave_map = cave.minimap

# for row in cave_map:
#     print(row)
