# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#
#  完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层
# 为第 h 层，则该层包含 1~ 2h 个节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：0
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：1
#
#
#
#
#  提示：
#
#
#  树中节点的数目范围是[0, 5 * 104]
#  0 <= Node.val <= 5 * 104
#  题目数据保证输入的树是 完全二叉树
#
#
#
#
#  进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
#  Related Topics 树 深度优先搜索 二分查找 二叉树
#  👍 567 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        完全二叉树只有两种情况，情况一：就是满二叉树，情况二：最后一层叶子节点没有满
        若最后一层不满则叶子节点只在最左侧
        """
        if not root: return 0
        left = root.left
        right = root.right
        left_height = 0
        right_height = 0
        while left:
            left = left.left
            left_height += 1

        while right:
            right = right.right
            right_height += 1

        if left_height == right_height:
            return (2 << left_height) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
