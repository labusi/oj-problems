#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (63.88%)
# Likes:    327
# Dislikes: 0
# Total Accepted:    40.8K
# Total Submissions: 63.9K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
# 返回如下的二叉树：
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder, inorder) -> TreeNode:
        return self.buildTree0(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def buildTree0(self, preorder, i, j, inorder, p, q):
        """根据preorder和inorder构造原来的树."""
        if i == j:
            return None
        node = TreeNode(preorder[i])
        m = inorder.index(preorder[i])
        node.left = self.buildTree0(preorder, i+1, i+1+m-p, inorder, p, m)
        node.right = self.buildTree0(preorder, i+1+m-p, j, inorder, m+1, q)
        return node


# @lc code=end
