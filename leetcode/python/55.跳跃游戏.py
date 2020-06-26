#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # target = len(nums) - 1
        # res = self.helper1(nums, 0, target)
        # return res
        return self.helper2(nums)

    def helper1(self, nums, idx, target):
        """
        超时.
        Args:
            nums: 数组
            idx: 当前位置
            target: 目标位置
        Returns:
            True: 能从当前位置到达目标位置
            False: 不能到达目标位置
        """
        if idx == target:
            return True

        for i in range(idx+1, idx+nums[idx]+1):
            res = self.helper1(nums, i, target)
            if res:
                return True

        return False

    def helper2(self, nums):
        """
        遍历一次, 维护一个rightmost, 即当前能到达的最远位置,
        如果遍历结束之后, rightmost依旧没有到达最后, 则返回False.
        """
        rightMost = 0
        n = len(nums)
        for i in range(n):
            if i <= rightMost: # i首先要在射程范围内
                rightMost = max(i+nums[i], rightMost)
            if rightMost >= n-1:
                return True
        return False
# @lc code=end
