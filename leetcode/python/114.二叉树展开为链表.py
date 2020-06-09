#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self._flatten(root)

    def _flatten(self, root):
        if root is None:
            return
        self._flatten(root.left)
        self._flatten(root.right)
        left = root.left
        right = root.right
        left_tail = left
        while left_tail is not None and left_tail.right is not None:
            left_tail = left_tail.right
        if left is None:
            return
        else:
            root.left = None
            root.right = left
            left_tail.right = right
# @lc code=end
