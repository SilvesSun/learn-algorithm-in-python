# coding=utf-8
# Definition for a  tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # @param root, a tree node
    # @return a boolean
    """
    在这道题里，平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于1。这实际上是AVL树的定义。
    首先要写一个计算二叉树高度的函数，二叉树的高度定义为：树为空时，高度为0。
        然后递归求解：树的高度 = max(左子树高度，右子树高度)+1(根节点要算上)。
    高度计算函数实现后，递归求解每个节点的左右子树的高度差，如果有大于1的，则return False。如果高度差小于等于1，则继续递归求解。
    """
    def height(self, root):
        if root is None: return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def is_balance(self, root):
        if root is None: return True
        if abs(self.height(root.left) - self.height(root.right)) <= 1:
            return self.is_balance(root.left) and self.is_balance(root.right)
        return False