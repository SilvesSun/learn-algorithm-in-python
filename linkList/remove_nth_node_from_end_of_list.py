# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first_point = head
        second_point = head

        i = 0
        while i < n:
            first_point = first_point.next
            i += 1
        if not first_point:
            return head.next

        while first_point.next:
            first_point = first_point.next
            second_point = second_point.next

        second_point.next = second_point.next.next
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s = Solution()
s.removeNthFromEnd(head, 2)




