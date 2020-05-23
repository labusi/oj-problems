#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    左右两个链表, 最后的结果合并即可.
    """
    def partition(self, head, x: int):
        left, right = ListNode(-1), ListNode(-1)
        p1, p2 = left, right

        while head is not None:
            val = head.val
            if val < x:
                p1.next = ListNode(val)
                p1 = p1.next
            else:
                p2.next = ListNode(val)
                p2 = p2.next
            head = head.next
        p1.next = right.next
        return left.next
# @lc code=end
