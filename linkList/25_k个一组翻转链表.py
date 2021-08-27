from datastructure.link_list import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # if not head or not head.next:
        #     return head
        # 先移动k步
        tail = head
        for i in range(k):
            if not tail:
                return head

            tail = tail.next
        new_head = self.reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return new_head

    def reverse(self, head: ListNode, tail: ListNode):
        pre = None
        while head != tail:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
