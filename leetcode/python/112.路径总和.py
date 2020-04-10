#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.find(root, sum)

    def find(self, root, sum):
        """
        递归求解.
        """
        if root is None:
            return False
        if root.left is None and root.right is None and sum==root.val:
            return True
        left = self.find(root.left, sum-root.val)
        if left:
            return True
        right = self.find(root.right, sum-root.val)
        if right:
            return True
        return False

# @lc code=end

