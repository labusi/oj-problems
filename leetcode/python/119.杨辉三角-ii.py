#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

from typing import List
# @lc code=start


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        for i in range(1, rowIndex+1):
            row = [0] * (i+1)
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = pre[j-1] + pre[j]
            pre = row
        return pre

# @lc code=end
