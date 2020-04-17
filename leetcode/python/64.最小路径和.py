#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1, y1 = i-1, j
                x2, y2 = i, j-1
                if x1 < 0 and y2 < 0:
                    dp[i][j] = grid[i][j]
                elif x1 < 0:
                    dp[i][j] = grid[i][j] + dp[x2][y2]
                elif y2 < 0:
                    dp[i][j] = grid[i][j] + dp[x1][y1]
                else:
                    dp[i][j] = grid[i][j] + min(dp[x1][y1], dp[x2][y2])

        return dp[m-1][n-1]

# @lc code=end

