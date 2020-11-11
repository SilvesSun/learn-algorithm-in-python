# coding=utf-8
class Solution(object):
    def inorder_non_recursive(self, root):
        if root is None:
            return []
        # 首先查找到最左子树, 用一个临时节点表示当前节点, 用一个列表存储遍历到的节点
        t_node = root
        node_list = []
        res = []
        while t_node or node_list:
            while t_node:
                node_list.append(t_node)
                t_node = t_node.left

            # 已经查找完成到最左子树
            t_node = node_list.pop()
            res.append(t_node.val)

            #  开始遍历右子树
            t_node = t_node.right

    def inorder_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.traverse(res, root)
        return res

    def traverse(self, res, node):
        if node:
            self.traverse(res, node.left)
            res.append(node.val)
            self.traverse(res, node.right)