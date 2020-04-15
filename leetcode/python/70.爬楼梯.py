#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        table = [0] * (n+1)
        table[1], table[2] = 1, 2
        for idx in range(3, n+1):
            table[idx] = table[idx-1] + table[idx-2]

        return table[n]
# @lc code=end
