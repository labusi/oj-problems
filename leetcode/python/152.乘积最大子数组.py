#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from typing import List

# @lc code=start


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        一维dp, dp[i]以nums[i]为结尾的答案.

        注意: 
            要求子数组连续;
            nums中可能有负数;
        """
        n = len(nums)
        dp1 = [num for num in nums] # 保存乘积最大
        dp2 = [num for num in nums] # 保存乘积最小
        ans = dp1[0]

        for i in range(1, n):
            a = dp1[i-1] * nums[i]
            b = dp2[i-1] * nums[i]
            if a < b:
                a, b = b, a
            if a > dp1[i]:
                dp1[i] = a
            if b < dp2[i]:
                dp2[i] = b
            if ans < dp1[i]:
                ans = dp1[i]
        return ans
# @lc code=end
