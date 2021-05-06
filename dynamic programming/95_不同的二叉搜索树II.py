class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        if n < 1:
            return []
        return self.g(1, n)

    def g(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        for i in range(start, end + 1):
            left = self.g(start, i - 1)
            right = self.g(i + 1, end)
            for ln in left:
                for rn in right:
                    r = TreeNode(i)
                    r.left = ln
                    r.right = rn
                    res.append(r)
        return res
