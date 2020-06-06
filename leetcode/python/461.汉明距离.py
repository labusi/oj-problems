#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        z = bin(x ^ y)
        for b in z:
            if b == '1':
                ans += 1

        return ans
# @lc code=end
