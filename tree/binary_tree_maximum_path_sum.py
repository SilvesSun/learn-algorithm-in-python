# coding:utf-8

"""
Given a tree, find the maximum path sum.
The path may start and end at any node in the tree.
For example:
Given the below tree,
       1
      / \
     2   3

Return6.

"""


class Solution(object):
    def __init__(self):
        self.max_sum = 0

    def max_path_sum(self, root):
        if root is None: return 0
        else:self.max_sum = root.val
        self.find_max_sum(root)
        return self.max_sum

    def find_max_sum(self, root):
        if root is None: return 0
        left = max(self.find_max_sum(root.left), 0)
        right = max(self.find_max_sum(root.right), 0)
        self.max_sum = max(self.max_sum, root.val+left+right)

        current = max(root.val, max(root.val+right, root.val+left))
        return current