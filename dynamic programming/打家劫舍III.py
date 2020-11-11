# Definition for a tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dic = {}
        return self.robSub(root, dic)

    def robSub(self, root, dic):
        if root is None: return 0
        if root in dic: return dic.get(root)

        val = 0
        if root.left is not None:
            val += self.robSub(root.left.left, dic) + self.robSub(root.left.right, dic)

        if root.right is not None:
            val += self.robSub(root.right.left, dic) + self.robSub(root.right.right, dic)

        val = max(val+root.val, self.robSub(root.left, dic)+self.robSub(root.right, dic))

        dic[root] = val
        return val

    def rob2(self, root):
        res = self.robSub2(root)
        return max(res[0], res[1])

    def robSub2(self, root):
        if not root: return [0, 0]

        left = self.robSub2(root.left)
        right = self.robSub2(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res
