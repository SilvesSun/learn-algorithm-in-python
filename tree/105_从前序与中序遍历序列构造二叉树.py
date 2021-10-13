# 给定一棵树的前序遍历 preorder 与中序遍历 inorder。请构造二叉树并返回其根节点。
#
#
#
#  示例 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
#  示例 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
#
#  提示:
#
#
#  1 <= preorder.length <= 3000
#  inorder.length == preorder.length
#  -3000 <= preorder[i], inorder[i] <= 3000
#  preorder 和 inorder 均无重复元素
#  inorder 均出现在 preorder
#  preorder 保证为二叉树的前序遍历序列
#  inorder 保证为二叉树的中序遍历序列
#
#  Related Topics 树 数组 哈希表 分治 二叉树
#  👍 1255 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return
        print(pre_start)
        root_val = preorder[pre_start]
        # root_val 在中序中的索引
        in_root_idx = inorder.index(root_val)
        root = TreeNode(root_val)
        left_size = in_root_idx - in_start
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size, inorder, in_start, in_root_idx - 1)
        root.right = self.build(preorder, pre_start + left_size + 1, pre_end, inorder, in_root_idx + 1, in_end)
        return root


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))
