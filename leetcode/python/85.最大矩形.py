#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
from typing import List
import copy


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) <=0 or len(matrix[0]) <=0:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_width = [[0]*n for _ in range(m)]
        # 初始化max_width
        for idx in range(m):
            if matrix[idx][0] == '1':
                max_width[idx][0] = 1
            for idy in range(1, n):
                if matrix[idx][idy] == '1':
                    max_width[idx][idy] = 1 + max_width[idx][idy-1]

        max_area = copy.deepcopy(max_width)
        anwser = max(max_area[0])
        for i in range(1, m):
            for j in range(n):
                width = max_width[i][j]
                for k in range(i, -1, -1):
                    height = (i - k) + 1
                    width = min(width, max_width[k][j])
                    area = height * width
                    if max_area[i][j] <= area:
                        max_area[i][j] = area
                        if max_area[i][j] > anwser:
                            anwser = max_area[i][j]
        return anwser


if __name__ == '__main__':
    matrix = [["0","0","0"],["0","0","0"],["1","1","1"]]

    s = Solution()
    a = s.maximalRectangle(matrix)
    print(a)
# @lc code=end
