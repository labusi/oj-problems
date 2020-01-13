#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start


class Solution:
    def findSubstring(self, s, words):
        if s == "" or words == []:
            return []
        res = []
        n = len(words)
        m = len(words[0])
        length = m * n
        start = 0
        word2num = {}
        for word in words:
            if word not in word2num:
                word2num[word] = 1
            else:
                word2num[word] += 1
        while start + length <= len(s):
            subs = s[start: start + length]
            if 1 == self.helper(subs, words, m, word2num.copy()):
                res.append(start)
            start += 1
        return res

    def helper(self, subs, words, m, word2num):
        for idx in range(0, len(subs), m):
            tmp_word = subs[idx: idx + m]
            if tmp_word not in word2num:
                return -1
            else:
                word2num[tmp_word] -= 1
                if word2num[tmp_word] < 0:
                    return -1
        return 1
# @lc code=end
