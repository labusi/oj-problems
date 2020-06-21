#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
from typing import List

# @lc code=start


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper2(board)

    def helper1(self, board):
        """
        使用额外的空间保存原始的细胞状态.
        """
        m, n = len(board), len(board[0])
        newBoard = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.calcStatus(board, newBoard, i, j)

        for i in range(m):
            for j in range(n):
                board[i][j] = newBoard[i][j]

    def calcStatus(self, board, newBoard, x, y):
        m, n = len(board), len(board[0])
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                # 不越界并且[i, j] != [x, y], 才是邻居.
                if i >= 0 and i < m and j >= 0 and j < n and not (i == x and j == y):
                    if board[i][j] == 1:
                        count += 1
        if board[x][y] == 1:
            if count == 2 or count == 3:
                newBoard[x][y] = 1
        else:
            if count == 3:
                newBoard[x][y] = 1

    def helper2(self, board):
        """
        设计中间状态:
        -1: 1 -> 0, 遍历某个细胞的邻居时, 如果邻居的状态是-1, 说明该邻居在初始时是1
         2: 0 -> 1
        """
        m, n = len(board), len(board[0])
        neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                     (0, 1), (1, -1), (1, 0), (1, 1))

        for i in range(m):
            for j in range(n):
                count = 0
                for neighbor in neighbors:
                    r, c = i+neighbor[0], j+neighbor[1]
                    # 不越界, 当前的邻居现在是活着的或者之前是活着的, count+=1
                    if (r >= 0 and r < m and c >= 0 and c < n) and abs(board[r][c]) == 1:
                        count += 1
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == -1:
                    board[i][j] = 0
# @lc code=end
