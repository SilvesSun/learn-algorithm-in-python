class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        sum -= root.val
        if (not root.left) and (not root.right):
            if sum == 0:
                return True
            else:
                return False
        if root.left and self.hasPathSum(root.left, sum): return True
        if root.right and self.hasPathSum(root.right, sum): return True
        return False
