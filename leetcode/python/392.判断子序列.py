#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        思路, 以此寻找s的第i个字符在t中的位置, 直到确定了s的最后一个字符的位置.
        """
        start = 0
        for i in range(len(s)):
            ch = s[i]
            old_start = start
            for j in range(start, len(t)):
                if t[j] == s[i]:
                    start = j + 1
                    break
            if old_start == start:
                return False
        return True


# @lc code=end
