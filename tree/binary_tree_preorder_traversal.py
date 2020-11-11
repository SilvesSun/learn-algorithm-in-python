# coding:utf-8


class Solution(object):
    def binary_tree_preorder_traversal(self, root):
        res = []
        if root is None:
            return []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res