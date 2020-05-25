#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
from typing import List
# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A or not A[0]:
            return None
        m, n = len(A), len(A[0])
        B = [[0]*m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                B[j][i] = A[i][j]
        return B
        
        
# @lc code=end

