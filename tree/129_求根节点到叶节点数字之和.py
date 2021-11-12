# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
#
#
#  每条从根节点到叶节点的路径都代表一个数字：
#
#
#  例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
#
#
#  计算从根节点到叶节点生成的 所有数字之和 。
#
#  叶节点 是指没有子节点的节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：25
# 解释：
# 从根到叶子节点路径 1->2 代表数字 12
# 从根到叶子节点路径 1->3 代表数字 13
# 因此，数字总和 = 12 + 13 = 25
#
#  示例 2：
#
#
# 输入：root = [4,9,0,5,1]
# 输出：1026
# 解释：
# 从根到叶子节点路径 4->9->5 代表数字 495
# 从根到叶子节点路径 4->9->1 代表数字 491
# 从根到叶子节点路径 4->0 代表数字 40
# 因此，数字总和 = 495 + 491 + 40 = 1026
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [1, 1000] 内
#  0 <= Node.val <= 9
#  树的深度不超过 10
#
#
#
#  Related Topics 树 深度优先搜索 二叉树
#  👍 438 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, res, [])
        return sum(map(lambda x: int(''.join(x)), res))

    def dfs(self, root, res, path):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append(path[:])
            return

        choices = []
        if root.left: choices.append(root.left)
        if root.right: choices.append(root.right)
        for choice in choices:
            self.dfs(choice, res, path)
            path.pop()


if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(9)
    node3 = TreeNode(0)
    node4 = TreeNode(5)
    node5 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    print(Solution().sumNumbers(node1))
