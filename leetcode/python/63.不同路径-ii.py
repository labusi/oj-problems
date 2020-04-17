#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

from typing import List


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0:
            return 1
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                x1, y1 = i - 1, j
                x2, y2 = i, j - 1
                if x1 >= 0:
                    dp[i][j] += dp[x1][y1]
                if y2 >= 0:
                    dp[i][j] += dp[x2][y2]
        return dp[m-1][n-1]
# @lc code=end

