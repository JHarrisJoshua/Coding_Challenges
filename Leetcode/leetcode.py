"""Leetcode"""
from typing import *
from collections import defaultdict, deque
from math import inf


# -------------------------------- 1. Two Sum -------------------------------- #
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, val in enumerate(nums):
            if (target - val) in values:
                return [i, values[target - val]]
            values[val] = i


# ------------------- 1162. As Far from Land as Possible --------------------- #
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, result = len(grid), -1
        dist_map = [[inf for _ in range(n)] for _ in range(n)]

        queue = deque([])
        for i, row in enumerate(grid):
            for j, val in enumerate(grid[i]):
                if val == 1:
                    dist_map[i][j] = 0
                    queue.append((i,j,0))

        while queue:
            row, col, dist = queue.popleft()

            for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                if not 0<=r<n or not 0<=c<n:
                    continue
                if grid[r][c] == 0 and dist+1 < dist_map[r][c]:
                    dist_map[r][c] = dist+1
                    result = max(result, dist+1)
                    queue.append((r, c, dist+1))

        return result
