#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0], ans = nums[0], nums[0]
        for i in range(1, n):
            dp[i] = nums[i] if dp[i-1] < 0 else nums[i] + dp[i-1]
            ans = dp[i] if ans < dp[i] else ans
        return ans
# @lc code=end

