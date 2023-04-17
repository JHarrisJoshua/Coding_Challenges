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

