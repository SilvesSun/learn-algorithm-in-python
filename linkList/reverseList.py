# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def reverseList2(self, head):
        if not head: return None
        new = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new
