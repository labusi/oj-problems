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
        dp[i], 保存到达第i个石子时, 上一跳距离的集合.
        lessions: 选择合适的数据结构, 比如此题的set; 减少不必要的循环;
        """
        if not stones or stones[1] > 1:
            return False

        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        dp[1].add(1)

        for i in range(2, n):
            for j in range(1, i):
                if not dp[j] or max(dp[j])+1 + stones[j] < stones[i]:
                    continue
                for step in dp[j]:
                    if stones[j] + step - 1 == stones[i]:
                        dp[i].add(step-1)
                    if stones[j] + step == stones[i]:
                        dp[i].add(step)
                    if stones[j] + step + 1 == stones[i]:
                        dp[i].add(step+1)

        return len(dp[-1]) != 0

# @lc code=end
