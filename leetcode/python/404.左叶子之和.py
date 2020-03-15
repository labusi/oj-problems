#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return Solution.sumOfLeftLeaves0(root)

    @staticmethod
    def sumOfLeftLeaves0(root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        elif root.left is None:
            return Solution.sumOfLeftLeaves0(root.right)
        elif root.left.left is None and root.left.right is None:
            return root.left.val + Solution.sumOfLeftLeaves0(root.right)
        else:
            a = Solution.sumOfLeftLeaves0(root.left)
            b = Solution.sumOfLeftLeaves0(root.right)
            return a + b


# @lc code=end
