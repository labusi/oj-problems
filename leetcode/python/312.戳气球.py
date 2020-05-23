#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

from typing import List

# @lc code=start


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        思路:
        每次选取nums[left]*nums[right]最大的元素删除.
        错了.
        """
        if not nums:
            return 0
        n, ans = len(nums), 0
        for _ in range(n):
            target_index, reward = -1, -1
            for j in range(len(nums)):
                # 找到left*right最大的元素
                left = 1 if j == 0 else nums[j-1]
                right = 1 if j == len(nums)-1 else nums[j+1]
                tmp_reward = left*right
                if tmp_reward > reward:
                    target_index = j
                    reward = tmp_reward
            ans += (reward * nums[target_index])
            del nums[target_index]
        return ans
# @lc code=end
