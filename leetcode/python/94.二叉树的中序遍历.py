#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        self.inorder0(root, res)
        return res

    def inorder0(self, root, res):
        """递归实现中序遍历"""
        if root is None:
            return
        self.inorder0(root.left, res)
        res.append(root.val)
        self.inorder0(root.right, res)

# @lc code=end
