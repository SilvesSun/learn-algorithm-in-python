# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # @param root, a tree node
    # @return an integer
    def min_depth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return self.min_depth(root.right) + 1
        if root.left is not None and root.right is None:
            return self.min_depth(root.left) + 1
        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1