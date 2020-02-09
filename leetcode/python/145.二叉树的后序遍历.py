#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (69.99%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 69.6K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [3,2,1]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        self.postorder0(root, res)
        return res

    def postorder0(self, root: TreeNode, res):
        if root is None:
            return
        self.postorder0(root.left, res)
        self.postorder0(root.right, res)
        res.append(root.val)

# @lc code=end
