#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        模拟加法.
        a, b, c, d分别表示a, b, 和, 进位.

        坑点:
            循环结束之后, 如果进位不为0, 应该将进位的值加入到结果中.
        """
        res = []
        i, j = len(num1)-1, len(num2)-1
        d = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                a = int(num1[i])
            else:
                a = 0
            if j >= 0:
                b = int(num2[j])
            else:
                b = 0

            c = a+b+d
            d = c//10
            res.insert(0, str(c % 10))
            i -= 1
            j -= 1
        else:
            if d != 0:
                res.insert(0, str(d))

        return ''.join(res)
# @lc code=end
