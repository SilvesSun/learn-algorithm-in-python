"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []

        def visit(node):
            if not root: return
            res.append(node.val)
            for i in range(len(node.children)):
                visit(node.children[i])
        visit(root)
        return res

    def preorder_iter(self, root):
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            res.append(node.val)
            for i in range(len(node.children)):
                q.extend(node.children)
        return res