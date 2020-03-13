#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []
        res = self.generateTrees0(1, n)
        return res

    def generateTrees0(self, a: int, b: int) -> List[TreeNode]:
        if a > b:
            return [None]
        if a == b:
            res = [TreeNode(a)]
            return res
        res = []
        for mid in range(a, b+1):
            left = self.generateTrees0(a, mid-1)
            right = self.generateTrees0(mid+1, b)
            for i in range(len(left)):
                for j in range(len(right)):
                    root = TreeNode(mid)
                    root.left = left[i]
                    root.right = right[j]
                    res.append(root)
        return res
# @lc code=end
