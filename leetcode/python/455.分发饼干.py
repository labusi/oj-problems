#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#
from typing import List

# @lc code=start


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        两个数组先排序, 然后使用双指针遍历.
        """
        g = sorted(g)
        s = sorted(s)
        n1, n2 = len(g), len(s)
        i, j = 0, 0
        ans = 0
        while i < n1 and j < n2:
            if g[i] <= s[j]:
                ans += 1
                i += 1
            # 不管饼干能不能满足孩子的胃口, j都要+1
            j += 1

        return ans


# if __name__ == "__main__":
#     g = [1, 1]
#     s = [2, 3, 1]
#     ans = Solution().findContentChildren(g, s)
#     print(ans)

# @lc code=end
