#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.height(root)

    def height(self, root):
        """计算树的深度."""
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max([left, right]) + 1
        
# @lc code=end

