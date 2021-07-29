from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pres = {}

        def helper(root, parent=None):
            if not root:
                return
            pres[root.val] = parent
            helper(root.left, root)
            helper(root.right, root)

        helper(root)
        ans = []

        def getDepth(root, parent=None, depth=0):
            if not root:
                return
            if depth == k:
                ans.append(root.val)
                return
            if root.left != parent:
                getDepth(root.left, root, depth + 1)
            if root.right != parent:
                getDepth(root.right, root, depth + 1)
            if pres[root.val] != parent:
                getDepth(pres[root.val], root, depth + 1)

        getDepth(target)

        return ans


