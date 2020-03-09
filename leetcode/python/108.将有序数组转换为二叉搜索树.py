#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
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
    '''
    找到序列的中位数, 作为根节点, 左边的部分递归构造左子树, 右边的部分递归构造右子树.
    '''

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None or len(nums) == 0:
            return None
        else:
            tree = self.sortedArrayToBST0(nums, 0, len(nums))
            return tree

    def sortedArrayToBST0(self, nums: List[int], i: int, j: int) -> TreeNode:
        if j - i == 1:
            return TreeNode(nums[i])
        if i == j:
            return None

        mid = (i + j) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST0(nums, i, mid)
        root.right = self.sortedArrayToBST0(nums, mid+1, j)

        return root

    # @lc code=end