#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
from typing import List

# @lc code=start


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        num_one = 0
        num_edge = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    num_one += 1
                    num_edge += self.count(i, j, m, n, grid)
        return num_one*4-num_edge

    def count(self, i, j, m, n, grid):
        ans = 0
        if j - 1 >= 0 and grid[i][j-1] == 1:
            ans += 1

        if j+1 < n and grid[i][j+1] == 1:
            ans += 1

        if i - 1 >= 0 and grid[i-1][j] == 1:
            ans += 1

        if i+1 < m and grid[i+1][j] == 1:
            ans += 1

        return ans

# @lc code=end
