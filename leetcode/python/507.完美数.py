#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

import math

# @lc code=start


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        测试用例里有1和小于0的数.
        """
        if num <= 1:
            return False

        s = 0
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                s += i + num//i

        s += 1

        if s == num:
            return True
        else:
            return False
# @lc code=end
