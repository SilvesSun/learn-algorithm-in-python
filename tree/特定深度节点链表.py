from collections import deque


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def list_of_depth(self, tree):
        """
        :type tree: TreeNode
        :rtype: List[ListNode]
        """
        if not tree:
            return []
        d = deque()
        d.append(tree)
        res = []
        while d:
            n = len(d)
            lnode = ListNode(None)
            cur = lnode
            for i in range(n):
                t_node = d.popleft()
                cur.next = ListNode(t_node.val)
                cur = cur.next
                if t_node.left:
                    d.append(t_node.left)
                if t_node.right:
                    d.append(t_node.right)
            res.append(lnode.next)
        return res