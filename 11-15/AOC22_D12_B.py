from collections import deque
from math import inf
from time_this import time_this


def bfs(file_name):
    board, cost_map, queue, target = [], [], deque([]), None
    with open(file_name, 'r') as infile:
        for i, line in enumerate(infile):
            board.append(list(line := line.strip()))
            cost_map.append([inf for _ in range(len(line))])
            for j, char in enumerate(line):
                if char in ['S', 'a']:
                    board[i][j] = cost_map[i][j] = 0
                    queue.append((0, i, j))
                elif char == 'E':
                    board[i][j] = ord('z') - ord('a')
                    target = (i, j)
                else:
                    board[i][j] = ord(board[i][j]) - ord('a')

    rows, cols = len(board), len(board[0])
    while queue:
        cost, row, col = queue.popleft()
        for r, c in [(row, col + 1), (row + 1, col),
                     (row, col - 1), (row - 1, col)]:
            if not 0<=r<rows or not 0<=c<cols:
                continue
            if (board[row][col]+1) < board[r][c]:
                continue
            if cost + 1 < cost_map[r][c]:
                queue.append((cost+1, r, c))
                cost_map[r][c] = cost + 1
            if (r, c) == target:
                return cost_map[r][c]


# Try DFS?
def dfs(file_name):
    board, cost_map, stack, target = [], [], [], None
    with open(file_name, 'r') as infile:
        for i, line in enumerate(infile):
            board.append(list(line := line.strip()))
            cost_map.append([inf for _ in range(len(line))])
            for j, char in enumerate(line):
                if char in ['S', 'a']:
                    board[i][j] = cost_map[i][j] = 0
                    stack.append((0, i, j))
                elif char == 'E':
                    board[i][j] = ord('z') - ord('a')
                    target = (i, j)
                else:
                    board[i][j] = ord(board[i][j]) - ord('a')

    rows, cols = len(board), len(board[0])
    while stack:
        cost, row, col = stack.pop()
        for r, c in [(row, col + 1), (row + 1, col),
                     (row, col - 1), (row - 1, col)]:
            if not 0<=r<rows or not 0<=c<cols:
                continue
            if (board[row][col]+1) < board[r][c]:
                continue
            if cost + 1 < cost_map[r][c]:
                stack.append((cost+1, r, c))
                cost_map[r][c] = cost + 1
            # if (r, c) == target:
            #     return cost_map[r][c]
    return cost_map[target[0]][target[1]]


@time_this
def time_trial(func):
    func("AOC22_D12_inp.txt")


if __name__ == '__main__':
    # Result & Time Trial
    print("BFS: ", bfs("AOC22_D12_inp.txt"))
    print(f'BFS trial: {time_trial(bfs)} seconds')

    print("DFS: ", dfs("AOC22_D12_inp.txt"))
    print(f'DFS trial: {time_trial(dfs)} seconds')
