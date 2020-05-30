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
        根据最后一个被戳破的气球构造状态转移关系.
        """
        n = len(nums) + 2
        nums = [1] + nums + [1]
        dp = [[0]*n for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                for k in range(i+1, j):
                    val = dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]
                    if val > dp[i][j]:
                        dp[i][j] = val

        return dp[0][-1]
# @lc code=end
