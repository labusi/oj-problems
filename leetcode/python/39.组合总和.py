#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

from typing import List
import copy

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(set(candidates))
        paths = []
        path = []
        self.helper(nums, 0, paths, path, target)
        return paths

    def helper(self, nums, start, paths, path, target):
        """
        以当前path为起点, 找到所有能够得到target的路径.
        """
        if target < 0:
            return
        if target == 0:
            paths.append(path[:])
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.helper(nums, i, paths, path, target-nums[i])
            if(len(path) > 0):
                path.pop()
            if target - nums[i] < 0:
                break
# @lc code=end
