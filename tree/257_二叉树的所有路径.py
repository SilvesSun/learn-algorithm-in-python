# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
#
#  叶子节点 是指没有子节点的节点。
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：["1"]
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [1, 100] 内
#  -100 <= Node.val <= 100
#
#  Related Topics 树 深度优先搜索 字符串 二叉树
#  👍 598 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List

import pylab as p


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.backtrack(root, res, [])
        return ["->".join(list(map(str, i))) for i in res]

    def backtrack(self, root, res, path):
        if not root:
            return []
        path.append(root.val)
        if not root.left and not root.right:
            # 说明是叶子节点
            res.append(path[:])
            return
        choices = []
        if root.left: choices.append(root.left)
        if root.right: choices.append(root.right)
        for choice in choices:
            self.backtrack(choice, res, path)
            path.pop()
