#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        path = []
        self.inOrder(root, path)
        self.fix(path)

    def inOrder(self, root, path):
        if root is None:
            return
        self.inOrder(root.left, path)
        path.append(root)
        self.inOrder(root.right, path)

    def fix(self, path):
        idx = []
        for i in range(len(path)-1):
            if path[i].val >= path[i+1].val:
                idx.append(i)
        if not idx:
            return

        a, b = idx[0], idx[-1] + 1
        tmp = path[a].val
        path[a].val = path[b].val
        path[b].val = tmp


# @lc code=end
