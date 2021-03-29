# Definition for a  tree node
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

    def min_depth2(self, root):
        if root is None: return 0
        nodes = [root]
        depth = 1
        while nodes:
            n = len(nodes)
            for i in range(n):
                node = nodes.pop(0)
                if (not node.left) and (not node.right):
                    return depth
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            depth += 1
        return depth