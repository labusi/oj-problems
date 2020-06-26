#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List

# @lc code=start


class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.helper2(nums)

    def helper1(self, nums):
        n = len(nums)
        dp = [0] + [1e64] * (n-1)
        for i in range(1, n):
            for j in range(i):
                if nums[j] + j >= i and dp[i] > dp[j] + 1:
                    dp[i] = dp[j]+1

        return dp[-1]

    def helper2(self, nums):
        """
        画图分析下.
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


# if __name__ == "__main__":
#     s = Solution()
#     nums = [2, 3, 1, 2, 4, 2, 3]
#     ans = s.jump(nums)
#     print(ans)

# @lc code=end
