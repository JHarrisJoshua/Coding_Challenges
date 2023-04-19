"""Leetcode"""
from typing import *
from collections import defaultdict, deque
from math import inf

# https://leetcode.com/JHarrisJoshua/


# -------------------- 1. Two Sum -------------------------------------------- #
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, val in enumerate(nums):
            if (target - val) in values:
                return [i, values[target - val]]
            values[val] = i


# -------------------- 59. Spiral Matrix II ---------------------------------- #
class Solution59:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(n)] for _ in range(n)]
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        idx = 0

        num, row, col = 1, 0, 0
        grid[row][col] = num
        num += 1

        while num <= n * n:
            r, c = row+moves[idx][0], col+moves[idx][1]
            while not(0<=r<n and 0<=c<n) or grid[r][c] > 0:
                idx = (idx+1) % 4
                r, c = row+moves[idx][0], col+moves[idx][1]
            grid[r][c] = num
            row, col, num = r, c, num + 1
        return grid


# --------------------- 63. Unique Paths II ---------------------------------- #
class Solution63:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        if grid[0][0] == 1: return 0

        dp[0][0] = 1
        for i, row in enumerate(grid):
            for j, val in enumerate(grid[i]):
                if val == 1 or (i, j) == (0, 0): continue
                if (i == 0 or j == 0):
                    dp[i][j] = (dp[i - 1][j] if j == 0 else dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# ------------------- 344. Reverse String ------------------------------------ #
class Solution344:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


# ------------------- 516. Longest Palindromic Subsequence ------------------- #
class Solution516:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2, n = s[::-1], len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i, row in enumerate(dp):
            for j, val in enumerate(dp[i]):
                if i==0 or j==0: continue
                if s[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1],
                                   dp[i-1][j])
        return dp[-1][-1]


# ------------------- 946. Validate Stack Sequences -------------------------- #
class Solution946:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        check_array, j = [], 0

        for i, val in enumerate(pushed):
            check_array.append(val)
            while check_array and check_array[-1] == popped[j]:
                check_array.pop()
                j += 1

        return not check_array


# ------------------- 1119. Remove Vowels from a String ---------------------- #
class Solution1119:
    def removeVowels(self, s: str) -> str:
        return "".join([char for char in s if char not in 'aeiou'])


# ------------------- 1162. As Far from Land as Possible --------------------- #
class Solution1162:
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


# ------------ 1372. Longest ZigZag Path in a Binary Tree -------------------- #
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1372:
    def longestZigZag(self, root: Optional[TreeNode],max_len=0) -> int:
        # (node, depth, move)
        # move: 0 is start, 1 is left, 2 is right
        stack = [(root, 0, 0)]

        while stack:
            curr, depth, move = stack.pop()
            max_len = max(max_len, depth)

            if curr.left:
                if move == 2:
                    stack.append((curr.left, depth+1, 1))
                else:
                    stack.append((curr.left, 1, 1))
            if curr.right:
                if move == 1:
                    stack.append((curr.right, depth+1, 2))
                else:
                    stack.append((curr.right, 1, 2))
        return max_len


# ------------ 1431. Kids With the Greatest Number of Candies ---------------- #
class Solution1431:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy, result = max(candies), []
        for i, candy in enumerate(candies):
            result.append(True if (candy + extraCandies >= max_candy) else False)
        return result


# ------------------- 1480. Running Sum of 1d Array -------------------------- #
class Solution1480:
    def runningSum(self, nums: List[int]) -> List[int]:
        result, run_sum = [], 0

        for i, val in enumerate(nums):
            run_sum += val
            result.append(run_sum)
        return result


# ------------------ 1768. Merge Strings Alternately ------------------------- #
class Solution1768:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n, res = len(word1), len(word2), []
        l = r = 0
        while l<m or r<n:
            res.append(word1[l] if l<m else "")
            res.append(word2[r] if r<n else "")
            l, r = l+1, r+1
        return "".join(res)


