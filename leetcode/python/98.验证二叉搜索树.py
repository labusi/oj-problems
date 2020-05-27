#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
遍历左子树, 检查是否全部的节点都小于根节点;
遍历右子树, 检查是否全部的节点都大于根节点;

检查左子树
检查右子树
"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # return self.checkPath(root)
        return self.inOrder2(root)

    def helper1(self, root):
        if root is None:
            return True

        left_valid = self.compare(root.left, root.val, 0)
        if not left_valid:
            return False
        right_valid = self.compare(root.right, root.val, 1)
        if not right_valid:
            return False

        left_valid = self.isValidBST(root.left)
        if not left_valid:
            return False
        right_valid = self.isValidBST(root.right)
        if not right_valid:
            return False
        return True

    def compare(self, root, target, op):
        """
        检查root为根的子树是否满足条件(全部的节点都应该满足op代表的条件).
        target: root的根节点
        op: 0表示root是左子树, 1表示root是右子树
        """
        if root is None:
            return True
        if (op == 0 and root.val >= target) or (op == 1 and root.val <= target):
            return False
        if not self.compare(root.left, target, op):
            return False
        if not self.compare(root.right, target, op):
            return False
        return True

    def inOrder(self, root, path):
        """
        通过中序遍历获得一个序列, 然后检查是否是升序.
        """
        if root is None:
            return
        self.inOrder(root.left, path)
        path.append(root.val)
        self.inOrder(root.right, path)

    def checkPath(self, root):
        path = []
        self.inOrder(root, path)
        for i in range(len(path)-1):
            if path[i] >= path[i+1]:
                return False
        return True

    def inOrder2(self, root):
        """
        通过非递归的方式进行中序遍历.
        使用栈保存, 0: 表示遍历当前节点, 1: 表示访问当前节点
        """
        if root is None:
            return True
        last_val = None
        s = [(root.right, 0), (root, 1), (root.left, 0)]
        while len(s) > 0:
            cur = s.pop()
            if cur[0] is None:
                continue
            elif cur[1] == 0:
                s.append((cur[0].right, 0))
                s.append((cur[0], 1))
                s.append((cur[0].left, 0))
            else:
                if last_val is None:
                    last_val = cur[0].val
                else:
                    if last_val >= cur[0].val:
                        return False
                    else:
                        last_val = cur[0].val
        return True
# @lc code=end
