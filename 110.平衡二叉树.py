#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return False if self.height(root) < 0 else True

    def height(self, root: TreeNode) -> int:
        """
        计算树的深度.
        """
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if left < 0 or right < 0 or abs(left-right) > 1:
            return -1
        return max([left, right]) + 1
# @lc code=end
