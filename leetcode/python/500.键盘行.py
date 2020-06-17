#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
from typing import List
# @lc code=start


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ans = []
        for word in words:
            word_lower = word.lower()
            lines = set()
            for ch in word_lower:
                idx = [i for i, key in enumerate(keys) if ch in key]
                lines.update(idx)
                if len(lines) > 1:
                    break
            if len(lines) == 1:
                ans.append(word)
        return ans

# @lc code=end
