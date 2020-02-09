#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (66.61%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    22.7K
# Total Submissions: 34.1K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
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
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        return self.buildTree0(inorder, 0, len(inorder), postorder, 0, len(postorder))

    def buildTree0(self, inorder, i, j, postorder, p, q):
        if i >= j:
            return None

        node = TreeNode(postorder[q-1])
        # 找到根节点
        m = inorder.index(postorder[q-1])
        # 构造左子树
        node.left = self.buildTree0(inorder, i, m, postorder, p, p+m-i)
        # 构造右子树
        node.right = self.buildTree0(inorder, m+1, j, postorder, q+m-j, q-1)
        return node


# @lc code=end
