#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        加法模拟.
        """
        p = 0
        arr = []
        # 当两个链表至少有一个非空时
        while l1 != None or l2 != None:
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val
            s = a + b + p
            if s >= 10:
                p = 1
            else:
                p = 0
            s %= 10
            self.appendNode(arr, ListNode(s))
            s = 0
            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
        if p == 1:
            self.appendNode(arr, ListNode(p))
        if len(arr) > 0:
            return arr[0]
        else:
            return None

    def appendNode(self, arr, node):
        """
        在尾部插入节点.
        """
        if len(arr) > 0:
            arr[-1].next = node
            arr.append(node)
        else:
            arr.append(node)


# @lc code=end
