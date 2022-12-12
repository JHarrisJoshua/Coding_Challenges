from collections import deque
from math import inf


def bfs(file_name):
    board = []
    with open(file_name, 'r') as infile:
        for line in infile:
            board.append(list(line.strip()))

    rows, cols = len(board), len(board[0])
    cost_map = [[inf for _ in range(cols)] for _ in range(rows)]
    queue, target = deque([]), None

    for i, row in enumerate(board):
        for j, val in enumerate(board[i]):
            if val in ['S', 'a']:
                board[i][j] = cost_map[i][j] = 0
                queue.append((0, i, j))
            elif val == 'E':
                target = (i, j)
                board[i][j] = ord('z') - ord('a')
            else:
                board[i][j] = ord(board[i][j]) - ord('a')
                
    while queue:
        cost, row, col = queue.popleft()
        for r, c in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
            if not 0<=r<rows or not 0<=c<cols:
                continue
            if (board[row][col]+1) < board[r][c]:
                continue
            if cost + 1 < cost_map[r][c]:
                queue.append((cost+1, r, c))
                cost_map[r][c] = cost + 1
            if (r, c) == target:
                return cost_map[r][c]


print(bfs("AOC22_D12_inp.txt"))
