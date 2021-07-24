class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node'):
        if not head:
            return head
        node_dict = {}
        p = head
        while p:
            cur = Node(p.val, None, None)
            node_dict[p] = cur
            p = p.next
        p = head
        while p:
            if p.next:
                node_dict[p].next = node_dict[p.next]
            if p.random:
                node_dict[p].random = node_dict[p.random]
            p = p.next
        return node_dict[head]




