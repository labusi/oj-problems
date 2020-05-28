#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
from typing import List

# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.helper1(nums)

    def helper1(self, nums):
        """
        一维dp.
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [1]*n
        ans = dp[0]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
            ans = dp[i] if ans < dp[i] else ans

        return ans
# @lc code=end
