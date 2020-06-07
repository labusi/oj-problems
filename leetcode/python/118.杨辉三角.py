#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List

# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(2, numRows+1):
            # 提前分配內存会提高执行效率
            row = [0]*i
            for j in range(0, i):
                if j == 0 or j == i-1:
                    row[j] = 1
                else:
                    row[j] = res[i-2][j-1]+res[i-2][j]
            res.append(row)
        return res
# @lc code=end
