#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, n
        while b-a > 1:
            m = (a+b)//2
            mv = isBadVersion(m)
            if mv is True:
                b = m
            else:
                a = m
        if isBadVersion(a):
            return a
        else:
            return b


# @lc code=end
