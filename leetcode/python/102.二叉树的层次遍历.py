#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (60.65%)
# Likes:    363
# Dislikes: 0
# Total Accepted:    75.1K
# Total Submissions: 123.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其层次遍历结果：
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        res = []
        q = queue.Queue()
        q.put(root)
        num1 = 1  # 记录当前层的节点个数
        num2 = 0  # 记录下一层的几点个数
        cur_level = []  # 记录当前层的
        while not q.empty():
            # 取出节点
            node = q.get()
            num1 -= 1
            # 读取节点的值, 添加子节点到下一层
            if node is not None:
                cur_level.append(node.val)
                q.put(node.left)
                q.put(node.right)
                num2 += 2
            if num1 == 0 and len(cur_level) > 0:
                res.append(cur_level)
                cur_level = []
                num1 = num2
                num2 = 0

        return res

# @lc code=end
