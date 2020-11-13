# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def level_order(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        q = [root]
        while q:
            length = len(q)
            level_res = []
            for i in range(length):
                r = q.pop(0)
                if r.left: q.append(r.left)
                if r.right: q.append(r.right)
                level_res.append(r.val)
            res.append(level_res)
        return res
