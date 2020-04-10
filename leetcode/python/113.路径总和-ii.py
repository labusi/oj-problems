#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        cur, paths = [], []
        self.find(root, sum, cur, paths)
        return paths

    def find(self, root: TreeNode, sum: int, cur: List[int], paths: List[List[int]]):
        if root is None:
            return
        if root.left is None and root.right is None and root.val == sum:
            cur.append(root.val)
            paths.append(cur.copy())
            cur.pop(-1)
            return
        cur.append(root.val)
        sum -= root.val
        self.find(root.left, sum, cur, paths)
        self.find(root.right, sum, cur, paths)
        cur.pop(-1)


# @lc code=end
