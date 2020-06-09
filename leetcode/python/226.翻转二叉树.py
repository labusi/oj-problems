#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        self._invertTree(root)
        return root

    def _invertTree(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self._invertTree(root.left)
        self._invertTree(root.right)

# @lc code=end
