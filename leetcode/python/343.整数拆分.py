#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # 分成2...n份
        ans = 0
        old_tmp = 0
        for i in range(2, n+1):
            if n % i == 0:
                a = n // i
                tmp = a**i
            else:
                a = n // i
                b = n % i
                tmp = (a+1)**b * a**(i-b)
            if tmp > ans:
                ans = tmp
            if old_tmp > tmp:
                break
            else:
                old_tmp = tmp
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     ans = s.integerBreak(8)
#     print(ans)
# @lc code=end
