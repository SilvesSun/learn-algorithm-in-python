# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
#  叶子节点 是指没有子节点的节点。
#
#
#
#
#
#  示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#
#
#  示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中节点总数在范围 [0, 5000] 内
#  -1000 <= Node.val <= 1000
#  -1000 <= targetSum <= 1000
#
#
#
#  Related Topics 树 深度优先搜索 回溯 二叉树
#  👍 610 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.path(root, res, [], targetSum)
        ans = list(filter(lambda x: sum(x) == targetSum, res))
        return ans

    def path(self, root, res, p, t):
        if not root:
            return []

        p.append(root.val)
        # 节点可能存在负数, 所以不能提前剪枝
        if not root.left and not root.right:
            res.append(p[:])
        choices = []
        if root.left: choices.append(root.left)
        if root.right: choices.append(root.right)
        for choice in choices:
            self.path(choice, res, p, t)
            p.pop()


if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(5)
    node10 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node4.left = node7
    node4.right = node8
    node3.left = node5
    node3.right = node6
    node6.left = node9
    node6.right = node10

    print(Solution().pathSum(node1, 22))