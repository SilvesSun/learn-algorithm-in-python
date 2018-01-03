# coding:utf-8


class Solution:
    def sum(self, root, pre_sum):
        if root is None:
            return 0
        pre_sum = pre_sum * 10 + root.val
        if root.left is None and root.right is None:
            return pre_sum
        return self.sum(root.left, pre_sum) + self.sum(root.right, pre_sum)

    def sum_numbers(self, root):
        return self.sum(root, 0)