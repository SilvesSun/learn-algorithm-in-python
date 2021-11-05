# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#
#
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#      1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#
#
#  进阶：
#
#  你可以运用递归和迭代两种方法解决这个问题吗？
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树
#  👍 1595 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.cmp(root.left, root.right)

    def cmp(self, left, right):
        if left and not right:
            return False
        elif not left and right:
            return False
        elif not left and not right:
            return True
        elif left.val != right.val:
            return False

        # 比较二叉树外侧是否对称：传入的是左节点的左孩子，右节点的右孩子
        out = self.cmp(left.left, right.right)
        # 比较内测是否对称，传入左节点的右孩子，右节点的左孩子
        inside = self.cmp(left.right, right.left)
        return out and inside