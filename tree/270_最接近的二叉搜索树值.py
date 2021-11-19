# 给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。
#
#  注意：
#
#
#  给定的目标值 target 是一个浮点数
#  题目保证在该二叉搜索树中只会存在一个最接近目标值的数
#
#
#  示例：
#
#  输入: root = [4,2,5,1,3]，目标值 target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# 输出: 4
#
#  Related Topics 树 深度优先搜索 二叉搜索树 二分查找 二叉树
#  👍 100 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_dif = float('INF')
    min_node = None

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        使用二进制搜索：如股票目标值小于当前根值，则向左搜索，否则向右搜索。在每一个步骤中选择最接近的值
        """
        if root:
            cur_diff = abs(root.val - target)
            if cur_diff < self.min_dif:
                self.min_dif = cur_diff
                self.min_node = root.val
            if target > root.val:
                self.min_node = self.closestValue(root.right, target)
            else:
                self.min_node = self.closestValue(root.left, target)
        return self.min_node


if __name__ == '__main__':
    node4 = TreeNode(4)
    node2 = TreeNode(2)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node4.left = node2
    node4.right = node5
    node2.left = node1
    node2.right = node3
    print(Solution().closestValue(node4, 3.714286))
