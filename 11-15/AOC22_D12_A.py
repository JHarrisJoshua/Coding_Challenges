from collections import deque
from math import inf


def main(file_name):
    board = []
    with open(file_name, 'r') as infile:
        for line in infile:
            line = list(line.strip().replace(' ', ''))
            board.append(line)

    rows, cols = len(board), len(board[0])
    costmap = [[inf for _ in range(cols)] for _ in range(rows)]
    queue = deque([])

    for i,row in enumerate(board):
        for j, val in enumerate(board[i]):
            if val in ['S', 'a']:
                board[i][j] = 0
                queue.append((i, j))
                costmap[i][j] = 0
            elif val == 'E':
                target = (i, j)
                board[i][j] = ord('z') - ord('a')
            else:
                board[i][j] = ord(board[i][j]) - ord('a')
    for row in board:
        print(row)
    print("____")

    while queue:
        row, col = queue.popleft()
        cost = costmap[row][col]
        for r, c in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
            if not 0<=r<rows or not 0<=c<cols:
                continue
            if board[r][c] > board[row][col] + 1:
                continue
            if cost + 1 < costmap[r][c]:
                queue.append((r,c))
                costmap[r][c] = cost + 1
            if (r,c) == target:
                rz, cz = target
                print(costmap[rz][cz])




    for row in costmap:
        print(row)

    rz, cz = target
    print(costmap[rz][cz])

print(main("AOC22_D12_inp.txt"))
