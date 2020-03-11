#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 递归出口, 根不相等/两个都是叶子节点
        lval = p.val if p is not None else None
        rval = q.val if q is not None else None
        if lval != rval:
            return False
        if p is None and q is None:
            return True

        # 比较left
        pleft = p.left if p is not None else None
        qleft = q.left if q is not None else None
        leftSame = self.isSameTree(pleft, qleft)
        if not leftSame:
            return False
        # 比较right
        pright = p.right if p is not None else None
        qright = q.right if q is not None else None
        rightSame = self.isSameTree(pright, qright)
        if not rightSame:
            return False
        return True


# @lc code=end
