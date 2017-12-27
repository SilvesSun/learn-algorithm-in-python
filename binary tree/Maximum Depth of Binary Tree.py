# coding:utf-8


class Solution(object):
    def max_depth(self, root):
        if root is None:
            return 0
        else:
            return max(self.max_depth(root.left), self.max_depth(root.right)) + 1