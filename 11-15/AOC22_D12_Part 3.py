from collections import deque
from math import inf
from time_this import time_this


def choose_your_own_adventure(file_name, adventure_type='bfs'):
    operation = {'bfs': lambda deck: deck.popleft(), 'dfs': lambda deck: deck.pop()}

    deck_the_halls_with_stacks_or_queues = deque([])

    board, cost_map, target = [], [], None
    with open(file_name, 'r') as infile:
        for i, line in enumerate(infile):
            board.append(list(line := line.strip()))
            cost_map.append([inf for _ in range(len(line))])
            for j, char in enumerate(line):
                if char in ['S', 'a']:
                    board[i][j] = cost_map[i][j] = 0
                    deck_the_halls_with_stacks_or_queues.append((0, i, j))
                elif char == 'E':
                    board[i][j] = ord('z') - ord('a')
                    target = (i, j)
                else:
                    board[i][j] = ord(board[i][j]) - ord('a')

    rows, cols = len(board), len(board[0])
    while deck_the_halls_with_stacks_or_queues:
        cost, row, col = operation[adventure_type](deck_the_halls_with_stacks_or_queues)
        for r, c in [(row, col + 1), (row + 1, col),
                     (row, col - 1), (row - 1, col)]:
            if not 0<=r<rows or not 0<=c<cols:
                continue
            if (board[row][col]+1) < board[r][c]:
                continue
            if cost + 1 < cost_map[r][c]:
                deck_the_halls_with_stacks_or_queues.append((cost+1, r, c))
                cost_map[r][c] = cost + 1
            if adventure_type == 'bfs' and (r, c) == target:
                return cost_map[r][c]
    return cost_map[target[0]][target[1]]  # For DFS


@time_this
def time_trial(func, type_of_traversal):
    func("AOC22_D12_inp.txt", type_of_traversal)


if __name__ == '__main__':
    # Result & Time Trial
    print("BFS: ", choose_your_own_adventure("AOC22_D12_inp.txt", 'bfs'))
    print(f'BFS trial: {time_trial(choose_your_own_adventure, "bfs")} seconds')

    print("DFS: ", choose_your_own_adventure("AOC22_D12_inp.txt", 'dfs'))
    print(f'DFS trial: {time_trial(choose_your_own_adventure, "dfs")} seconds')
