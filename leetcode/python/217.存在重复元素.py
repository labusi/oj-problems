#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
from typing import List

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        N = len(nums)
        s.update(nums)
        N_ = len(s)
        return N > N_
# @lc code=end
