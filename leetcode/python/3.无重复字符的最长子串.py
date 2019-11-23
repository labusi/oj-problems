#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        动态规划求解.
        s[i]: 保存以s的第i的字符为结尾的最长无重复子串.
        """
        if s == None or s == "":
            return 0
        maxlen = [s[0]]
        res = 1
        for i in range(1, len(s)):
            index = maxlen[-1].find(s[i])
            if index != -1:
                maxlen.append(maxlen[-1][index+1:] + s[i])
            else:
                maxlen.append(maxlen[-1] + s[i])
            res = len(maxlen[-1]) if len(maxlen[-1]) > res else res
        return res


# @lc code=end
