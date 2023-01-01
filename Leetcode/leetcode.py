"""Leetcode"""
from typing import *
import collections
from math import inf


# ---- 1 - Two Sum --- #
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, val in enumerate(nums):
            if (target - val) in values:
                return [i, values[target - val]]
            values[val] = i
