#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#
from typing import List

# @lc code=start

"""
动态规划的思路:
    dp[i, j].fir, dp[i, j].sec分别表示去区间[i,j]内的石子时, 先手和后手取得的最大分数.
    dp[i, j].fir = max{piles[i] + dp[i+1, j].sec, piles[j] + dp[i, j-1].sec}
    先手和后手的转换, 是关键.
"""


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

    def helper(self, piles):

        class Item:
            def __init__(self):
                self.fir, self.sec = 0, 0

        n = len(piles)
        dp = [[Item() for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i].fir = piles[i]

        for i in range(1, n):
            for j in range(n-i):
                a, b = j, j+i
                left = piles[a] + dp[a+1][b].sec
                right = piles[b] + dp[a][b-1].sec
                if left < right:
                    dp[a][b].fir = right
                    dp[a][b].sec = dp[a][b-1].fir
                else:
                    dp[a][b].fir = left
                    dp[a][b].sec = dp[a+1][b].fir

        return dp[0][n-1].fir - dp[0][n-1].sec


# @lc code=end
