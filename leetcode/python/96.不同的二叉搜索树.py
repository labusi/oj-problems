#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        res = [1, 1, 2, 5]
        if n <= 3:
            return res[n]
        else:
            for i in range(4, n+1):
                s = 0
                for j in range(0, i):
                    s += (res[j] * res[i-1-j])
                res.append(s)
        return res[-1]
# @lc code=end
