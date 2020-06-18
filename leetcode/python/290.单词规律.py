#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        思路:
            pattern中的字符和单词必须是11映射关系.
        """
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        table1 = {}
        table2 = {}

        for p, w in zip(pattern, words):
            w_val = table1.get(p)
            p_val = table2.get(w)
            if w_val is not None and w_val != w:
                return False
            if p_val is not None and p_val != p:
                return False
            if p_val is None and w_val is None:
                table1[p] = w
                table2[w] = p
        return True


if __name__ == "__main__":
    pattern = "abab"
    s = "dog cat dog cat"
    sl = Solution()
    ans = sl.wordPattern(pattern, s)
    print(ans)
# @lc code=end
