# coding:utf-8


class Solution(object):
    def connect(self, root):
        if root is None: return
        if root.left is not None: root.left.next = root.right
        if root.right is not None:
            if root.next is not None:
                root.right.next = root.next.left
            else:
                root.right.next = None
        self.connect(root.left)
        self.connect(root.right)