#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p1, p2 = head, head

        while p2 is not None:
            p2 = p2.next
            if p2 == p1:
                break
            p2 = None if p2 is None else p2.next
            if p2 == p1:
                break
            p1 = p1.next

        return p2 is not None
            
        
# @lc code=end

