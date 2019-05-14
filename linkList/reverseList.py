# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next


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


p = ListNode(1, ListNode(2, ListNode(3, None)))
q = Solution().reverseList(p)
while q:
    print(q.val)
    q = q.next
