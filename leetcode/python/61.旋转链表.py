#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        # 处理特殊情况
        if head == None:
            return None
        cur = head
        # 记录链表元素个数
        n = 1
        while cur.next != None:
            cur = cur.next
            n += 1
        # 构造循环链表
        cur.next = head

        steps = n - k % n - 1
        cur = head
        for _ in range(steps):
            cur = cur.next
        res = cur.next
        cur.next = None
        return res


# @lc code=end
