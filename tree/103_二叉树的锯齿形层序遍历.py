# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#  例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回锯齿形层序遍历如下：
#
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
#  Related Topics 树 广度优先搜索 二叉树
#  👍 541 👎 0


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return []

        q = [root]
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                level.append(node.val)
            if len(res) % 2 == 1:
                res.append(level)
            else:
                res.append(level[::-1])
        return res


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(10)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    print(Solution().zigzagLevelOrder(node1))