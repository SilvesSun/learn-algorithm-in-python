# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.left is None and root.right is None: return root

        if root.left and root.right:
            left = root.left
            right = root.right
            root.left = self.invertTree(right)
            root.right = self.invertTree(left)

        if root.left is None:
            root.left = self.invertTree(root.right)
            root.right = None
        if root.right is None:
            root.right = self.invertTree(root.left)
            root.left = None
        return root


