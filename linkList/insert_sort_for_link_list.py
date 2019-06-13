# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        if head.next is None: return head

        help_node = ListNode(0)
        while head is not None:
            node = help_node
            fol = head.next
            while node.next is not None and node.next.val < head.val:
                node = node.next
            head.next = node.next
            node.next = head
            head = fol
        return help_node.next

