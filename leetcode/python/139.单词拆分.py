#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

from typing import List

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[False]*(n+1) for _ in range(n+1)]
        for idx in range(1, n+1):
            for i in range(0, n+1-idx):
                if s[i:i+idx] in wordDict:
                    dp[i][i+idx] = True
                    continue
                for j in range(i+1, i+idx):
                    if dp[i][j] and dp[j][i+idx]:
                        dp[i][i+idx] =True
                        continue

        return dp[0][n]
# @lc code=end

