#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

from typing import List

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        return self.helper1(stones)

    def helper1(self, stones):
        """
        超时.
        思路: 
            dp[i]是一个列表, i表示第i个石子, dp[i]中保存的是上一跳步长的所有可能结果, 不考虑上一跳的起点.
        根据dp[i]中的元素, 就可以计算出从当前位置能跳到的所有可能的下一个石子, 并且更新对应石子的dp.
        """
        if not stones or stones[1] > 1:
            return False

        n = len(stones)
        dp = [[] for _ in range(n)]
        dp[0].append(0)
        for i in range(0, n - 1):
            for k in dp[i]:
                if k - 1 > 0:
                    next = stones[i] + k - 1
                    if next in stones:
                        dp[stones.index(next)].append(k - 1)
                if k > 0:
                    next = stones[i] + k
                    if next in stones:
                        dp[stones.index(next)].append(k)
                next = stones[i] + k + 1
                if next in stones:
                    dp[stones.index(next)].append(k + 1)

        return len(dp[-1]) != 0


# @lc code=end
