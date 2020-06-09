#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        dp = [num for num in nums]
        ans = max(dp)
        for i in range(2, len(nums)):
            for j in range(0, i-1):
                if nums[i] + dp[j] > dp[i]:
                    dp[i] = nums[i]+dp[j]
            if dp[i] > ans:
                ans = dp[i]
        return ans
# @lc code=end
