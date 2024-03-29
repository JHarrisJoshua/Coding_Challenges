"""Leetcode"""
from typing import *
from collections import defaultdict, deque
from math import inf
from heapq import heappop, heappush
import heapq


# https://leetcode.com/JHarrisJoshua/


# ------------ Definition for a binary tree node ----------------------------  #
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


# ---------------------- 62. Unique Paths ------------------------------------ #
class Solution62:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m

        for i, row in enumerate(dp):
            for j, cell in enumerate(dp[0]):
                dp[i][j] = (1 if i==0 or j==0
                            else dp[i-1][j]+dp[i][j-1])
        return dp[-1][-1]


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


# -------------------- 75. Sort Colors --------------------------------------- #
class Solution75:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, n = 0, len(nums) - 1, len(nums)

        i = 0
        while i < n and left < right and i <= right:
            i = max(i, left)
            num = nums[i]
            if nums[left] == 0:
                left += 1
            elif nums[right] == 2:
                right -= 1
            elif num == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif num == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1


# ------------- 119. Pascal's Triangle II ---------------------------- #
class Solution119:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            result.append(math.comb(rowIndex, i))
        return result

# ------------- 128. Longest Consecutive Sequence ---------------------------- #
class Solution128:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, hashset = 0, set(nums)

        while hashset:
            curr, num = 1, hashset.pop()
            plus, minus = num + 1, num - 1
            while plus in hashset:
                hashset.remove(plus)
                curr += 1
                plus += 1
            while minus in hashset:
                hashset.remove(minus)
                curr += 1
                minus -= 1
            res = max(res, curr)
        return res


# ------------------- 169. Majority Element ---------------------------------- #
class Solution169:
    def majorityElement(self, nums: List[int]) -> int:
        count, curr = 0, -inf

        for i, num in enumerate(nums):
            if num == curr:
                count += 1
            elif count == 0:
                count, curr = 1, num
            else:
                count -= 1

        return curr

# ------------------- 217. Contains Duplicate -------------------------------- #
class Solution217:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


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


# ------------------- 366. Find Leaves of Binary Tree ------------------------ #
class Solution366:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree_nodes = []

        def get_height(node):
            if not node:
                return -1

            height = max(get_height(node.left), get_height(node.right)) + 1

            if len(tree_nodes) == height:
                tree_nodes.append([])
            tree_nodes[height].append(node.val)
            return height

        get_height(root)
        return tree_nodes


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


# ------------------- 662. Maximum Width of Binary Tree ---------------------- #
class Solution662:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0, 1)])
        max_radius, level, left, right = 0, 0, inf, -inf

        while queue:
            curr, depth, value = queue.popleft()
            if depth > level:
                level, left, right = depth, inf, -inf

            left, right = min(left, value), max(right, value)
            max_radius = max(max_radius, right-left+1)

            if curr.left:
                queue.append((curr.left, depth+1, value*2-1))
            if curr.right:
                queue.append((curr.right, depth+1, value*2))
        return max_radius


# ---------------------- 771. Jewels and Stones ---------------------------- #
class Solution771:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        res = 0

        for char in stones:
            if char in jewels:
                res += 1
        return res


# ------------------- 933. Number of Recent Calls -------------------------- #
class RecentCounter:
    def __init__(self):
        self.queue = deque([])

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < (t-3000):
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)


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


# ----------------------- 1046. Last Stone Weight ---------------------------- #
class Solution1046:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap
        stones = [-wei for wei in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y, x = -heapq.heappop(stones), -heapq.heappop(stones)
            if y > x:
                heapq.heappush(stones, -y+x)
        return abs(stones[0]) if stones else 0


# ------------------- 1119. Remove Vowels from a String ---------------------- #
class Solution1119:
    def removeVowels(self, s: str) -> str:
        return "".join([char for char in s if char not in 'aeiou'])


# ----------------------- 1165. Single-Row Keyboard -------------------------- #
class Solution1165:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap, res = dict(), 0
        for i, char in enumerate(keyboard):
            hashmap[char] = i

        for i, char in enumerate(word):
            res += abs(hashmap[char] - (0 if i == 0 else hashmap[word[i - 1]]))
        return res

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


# ---------------------- 1470. Shuffle the Array ---------------------------- #
class Solution1470:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        left, right = 0, n
        for i in range(n):
            res.append(nums[left]), res.append(nums[right])
            left, right = left+1, right+1
        return res


# --------------------- 1476. Subrectangle Queries --------------------------- #
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.grid = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.grid[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.grid[row][col]


# ------------------- 1480. Running Sum of 1d Array -------------------------- #
class Solution1480:
    def runningSum(self, nums: List[int]) -> List[int]:
        result, run_sum = [], 0

        for i, val in enumerate(nums):
            run_sum += val
            result.append(run_sum)
        return result


# ------------------- 1512. Number of Good Pairs ---------------------------- #
class Solution1512:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap, res = defaultdict(list), 0

        for i, num in enumerate(nums):
            if num in hashmap:
                res += len(hashmap[num])
            hashmap[num].append(i)
        return res

# ------------------- 1603. Design Parking System ---------------------------- #
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.types = {1: self.big, 2: self.medium, 3: self.small}

    def addCar(self, carType: int) -> bool:
        if self.types[carType] > 0:
            self.types[carType] -= 1
            return True
        return False


# ----- 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers -------- #
    def minPartitions(self, n: str) -> int:
        return int(max(n))


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


# --------------- 1874. Minimize Product Sum of Two Arrays ------------------- #
class Solution1874:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        def counting_sort(arr, desc=False):
            arr_min, arr_max = inf, -inf
            for i, val in enumerate(arr):
                arr_min = min(arr_min, val)
                arr_max = max(arr_max, val)
            range_arr = [0] * (arr_max - arr_min + 1)

            for i, val in enumerate(arr):
                range_arr[val - arr_min] += 1

            idx = (len(arr) - 1) if desc else 0
            move = -1 if desc else 1
            for i, val in enumerate(range_arr):
                for j in range(val):
                    arr[idx] = arr_min + i
                    idx += move

        counting_sort(nums1)
        counting_sort(nums2, True)
        result = 0
        for i, val in enumerate(nums1):
            result += val * nums2[i]

        return result


# ----------------- 2336. Smallest Number in Infinite Set -------------------- #
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

class SmallestInfiniteSet:
    def __init__(self):
        self._heap = []
        self._set = set()
        self._largest = 1

    def popSmallest(self) -> int:
        if not self._heap:
            res = self._largest
            self._largest += 1
            return res
        if self._heap:
            res = heappop(self._heap)
            self._set.remove(res)
            return res

    def addBack(self, num: int) -> None:
        if num >= self._largest or num in self._set:
            return
        heappush(self._heap, num)
        self._set.add(num)


# ----------------- 2469. Convert the Temperature -------------------- #
class Solution2469:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]


# ----------------- 2658. Maximum Number of Fish in a Grid -------------------- #
class Solution2658:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        feesh, rows, cols = 0, len(grid), len(grid[0])

        def gotta_catch_em_all(spot):
            stacked, catch = [spot], 0
            while stacked:
                r, c = stacked.pop()
                catch += grid[r][c]
                grid[r][c] = 0

                for row, col in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if not (0<=row<rows and 0<=col<cols):
                        continue
                    if grid[row][col] > 0:
                        stacked.append((row,col))
            return catch

        for i, row in enumerate(grid):
            for j, val in enumerate(grid[i]):
                if val > 0:
                    feesh = max(feesh, gotta_catch_em_all((i,j)))
        return feesh
