#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        最长的回文串, 统计输入的每个字符的个数, 按照奇数和偶数分别进行处理.
        """
        vocab = {}
        for ch in s:
            vocab[ch] = vocab.get(ch, 0) + 1

        odd = sorted([it for it in vocab.values() if it %
                      2 == 1], reverse=True)
        a = 0
        for i, v in enumerate(odd):
            if i == 0:
                a += v
            else:
                a += v-1

        even = sum([it for it in vocab.values() if it % 2 == 0])

        return a + even


# @lc code=end
