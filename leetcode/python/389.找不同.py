#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        table_s = {}
        table_t = {}
        for c in s:
            table_s[c] = table_s.get(c, 0) + 1
        for c in t:
            table_t[c] = table_t.get(c, 0) + 1
        for it in table_t.items():
            vt = it[1]
            vs = table_s.get(it[0], 0)
            if vt != vs:
                return it[0]


if __name__ == "__main__":
    s = Solution()
    ans = s.findTheDifference('ab', 'bac')
    print(ans)

# @lc code=end
