# Definition for a tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = -1

        def diameter(root):
            if root is None:
                return 0
            left = diameter(root.left)
            right = diameter(root.right)
            length = left + right + 1
            self.result = max(self.result, length)
            return max(left, right) + 1

        diameter(root)
        return 0 if self.result == -1 else self.result - 1


