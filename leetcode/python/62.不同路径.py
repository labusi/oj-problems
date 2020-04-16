#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                x1, y1 = i - 1, j
                x2, y2 = i, j - 1
                if x1 >= 0:
                    dp[i][j] += dp[x1][y1]
                if y2 >= 0:
                    dp[i][j] += dp[x2][y2]
        return dp[m-1][n-1]

# @lc code=end

