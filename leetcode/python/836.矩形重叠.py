#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#

# @lc code=start
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = min(rec1[0], rec2[0])
        y1 = min(rec1[1], rec2[1])

        x2 = max(rec1[2], rec2[2])
        y2 = max(rec1[3], rec2[3])

        s1x = (rec1[2] - rec1[0])
        s2x = (rec2[2] - rec2[0])
        s1y = (rec1[3] - rec1[1])
        s2y = (rec2[3] - rec2[1])

        return s1x + s2x > x2 - x1 and s1y + s2y > y2 - y1

# @lc code=end
