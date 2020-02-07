#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num1 = x
        num2 = 0

        while x > 0:
            rest = x % 10
            num2 = num2 * 10 + rest
            x //= 10

        return num1 == num2

# @lc code=end
