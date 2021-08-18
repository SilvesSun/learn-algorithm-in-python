import heapq
from typing import List

from datastructure.link_list import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]

        heap = []
        cur = dummy = ListNode(-1)
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        return dummy.next