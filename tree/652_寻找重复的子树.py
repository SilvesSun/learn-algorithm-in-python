# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
#  两棵树重复是指它们具有相同的结构以及相同的结点值。
#
#  示例 1：
#
#          1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
#
#
#  下面是两个重复的子树：
#
#        2
#      /
#     4
#
#
#  和
#
#      4
#
#
#  因此，你需要以列表的形式返回上述重复子树的根结点。
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树
#  👍 322 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        看到这个问题，就可以判断本题要使用「后序遍历」框架来解决
        为什么？很简单呀，我要知道以自己为根的子树长啥样，是不是得先知道我的左右子树长啥样，再加上自己，就构成了整棵子树的样子
        """
        res = []
        map = {}
        self.traverse(root, map, res)
        return res

    def traverse(self, node, map, res):
        if node is None:
            return '#'
        left = self.traverse(node.left, map, res)
        right = self.traverse(node.right, map, res)
        sub = left + ',' + right + ',' + str(node.val)
        if map.get(sub, 0) == 1:
            res.append(node)
        if sub not in map:
            map[sub] = 1
        else:
            map[sub] += 1
        return sub