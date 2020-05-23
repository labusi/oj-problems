#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        new_head = head
        while head.next is not None:
            p = head.next
            head.next = p.next
            p.next = new_head
            new_head = p
        return new_head
# @lc code=end
