# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不
# 一定经过根节点。
#
#  路径和 是路径中各节点值的总和。
#
#  给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
#  示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
#
#
#  提示：
#
#
#  树中节点数目范围是 [1, 3 * 10⁴]
#  -1000 <= Node.val <= 1000
#
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 1395 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        一颗三个节点的小树的结果只可能有如下6种情况：
        根 + 左 + 右
        根 + 左
        根 + 右
        根
        左
        右

        好了，分析上述6种情况， 只有 2,3,4 可以向上累加，而1,5,6不可以累加（这个很好想，情况1向上累加的话，必然出现分叉，情况5和6直接就跟上面的树枝断开的，没法累加）
        所以我们找一个全局变量存储 1,5,6这三种不可累加的最大值， 另一方面咱们用遍历树的方法求2,3,4这三种可以累加的情况。 最后把两类情况得到的最大值再取一个最大值即可
        """
        self.max_sum = -sys.maxsize - 1

        def scan(root):
            if root is None:
                return -sys.maxsize - 1
            left = scan(root.left)
            right = scan(root.right)
            self.max_sum = max(self.max_sum, root.val + left + right, left, right)  # 情况1,5,6，不累加直接放变量里暂存
            return max(root.val, root.val + left, root.val + right)  # 情况2,3,4 ，累加需要递归

        new_max = scan(root)
        return max(self.max_sum, new_max)  # 两类情况再求最大

# leetcode submit region end(Prohibit modification and deletion)
