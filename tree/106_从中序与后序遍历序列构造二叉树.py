# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  Related Topics 树 数组 哈希表 分治 二叉树
#  👍 598 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder, in_start, in_end, postorder, post_start, post_end):
        if in_start > in_end:
            return
        root_val = postorder[post_end]
        idx = inorder.index(root_val)
        left_size = idx - in_start
        root = TreeNode(root_val)
        root.left = self.build(inorder, in_start, idx - 1, postorder, post_start, post_start + left_size - 1)
        root.right = self.build(inorder, idx + 1, in_end, postorder, post_start + left_size, post_end - 1)
        return root
# leetcode submit region end(Prohibit modification and deletion)
