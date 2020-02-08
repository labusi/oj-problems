#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 是叶子节点返回1
        if root.left is None and root.right is None:
            return 1
        left, right = None, None
        if root.left is not None:
            left = 1 + self.minDepth(root.left)
        if root.right is not None:
            right = 1 + self.minDepth(root.right)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return left if left < right else right


# @lc code=end
