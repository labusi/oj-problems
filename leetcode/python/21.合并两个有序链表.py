#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        cur = head
        while not (l1 == None and l2 == None):
            if l1 == None:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
            cur = cur.next
        return head.next

# @lc code=end
