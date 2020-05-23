#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        mem = set()
        while head is not None:
            if head in mem:
                return head
            else:
                mem.add(head)
            head = head.next
        return None

# @lc code=end
