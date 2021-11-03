# 给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。
#
#  进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？
#
#
#
#  示例 1：
#
#
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
#
#
#  示例 2：
#
#
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
#
#
#
#  提示：
#
#
#  树上节点的数目在范围 [2, 1000] 内
#  -231 <= Node.val <= 231 - 1
#
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树
#  👍 582 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        二叉搜索树，我们知道如果对其进行中序遍历，得到的值序列是递增有序的
        """
        nodes = []

        # 中序遍历二叉树，并将遍历的结果保存到list中
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)

        dfs(root)
        x = None
        y = None
        pre = nodes[0]
        # 扫面遍历的结果，找出可能存在错误交换的节点x和y
        for i in range(1, len(nodes)):
            if pre.val > nodes[i].val:
                y = nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树
        if x and y:
            x.val, y.val = y.val, x.val