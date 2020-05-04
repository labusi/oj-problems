#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List
import collections


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.bfs(grid)

    def basic(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        id = 1

        xy2id, id2xy = {}, {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    top = xy2id.get((i - 1, j))
                    left = xy2id.get((i, j - 1))
                    if top is None and left is None:
                        xy2id[(i, j)] = id
                        id2xy[id] = [(i, j)]
                        id += 1
                    elif top is None and left is not None:
                        xy2id[(i, j)] = left
                        id2xy[left].append((i, j))
                    elif top is not None and left is None:
                        xy2id[(i, j)] = top
                        id2xy[top].append((i, j))
                    else:
                        if top == left:
                            xy2id[(i, j)] = top
                        else:
                            # 以top为基准
                            xy2id[(i, j)] = top
                            for xy in id2xy[left]:
                                xy2id[xy] = top
                            id2xy[top] += id2xy[left]
                            del id2xy[left]
                        id2xy[top].append((i, j))

        return len(id2xy.keys())

    def bfs(self, grid):
        """
        广度优先搜索.
        遇到的1都标记为0, 搜索的次数即为岛屿的个数.
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        ans = 0

        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    q.append((i, j))
                    grid[i][j] = "0"
                    ans += 1
                    while q:
                        x, y = q.popleft()
                        if x > 0 and grid[x - 1][y] == "1":
                            grid[x - 1][y] = "0"
                            q.append((x - 1, y))
                        if x < m - 1 and grid[x + 1][y] == "1":
                            grid[x + 1][y] = "0"
                            q.append((x + 1, y))
                        if y > 0 and grid[x][y - 1] == "1":
                            grid[x][y - 1] = "0"
                            q.append((x, y - 1))
                        if y < n - 1 and grid[x][y + 1] == "1":
                            grid[x][y + 1] = "0"
                            q.append((x, y + 1))

        return ans


if __name__ == "__main__":
    grid = [
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "1"],
    ]
    s = Solution()
    ans = s.numIslands(grid)
    print(ans)
# @lc code=end
