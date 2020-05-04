#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a, c = 1, 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            b = digits[i]
            d = a + b + c
            c = d // 10
            b = d % 10
            a = 0
            digits[i] = b

        if c > 0:
            digits.insert(0, c)
        return digits


# @lc code=end
