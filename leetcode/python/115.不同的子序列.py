#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    """
    思路:
    取s的前i个字符为ss, t的前j个字符为tt, ss的全部子序列中包含的tt的个数记作dp[i,j].
    
    1) 当s[i] == t[j]: 
        dp[i,j] = dp[i-1, j-1] + dp[i-1, j]
        此时dp[i, j]由两部分组成, 第一部分是包含s[i]的子序列数量, 第二部分是不包含s[i]的子序列数量
    2) 否则:
        dp[i, j] = dp[i-1, j] 
    """

    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1 : i] == t[j - 1 : j]:
                    if j - 1 == 0:
                        a = 1
                    else:
                        a = dp[i - 1][j - 1]
                    b = dp[i - 1][j]
                    dp[i][j] = a + b
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


# @lc code=end
