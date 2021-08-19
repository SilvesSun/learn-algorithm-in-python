from datastructure.link_list import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 让两个指针slow和fast分别指向链表头结点head。
        #
        # 每当慢指针slow前进一步，快指针fast就前进两步，这样，当fast走到链表末尾时，slow就指向了链表中点
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow