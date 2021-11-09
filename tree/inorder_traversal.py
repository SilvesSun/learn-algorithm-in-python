# coding=utf-8
from tree.util import TreeNode


class Solution(object):
    def inorder_non_recursive(self, root):
        """
        解题思路：假设树为：

　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　/　  \

　　　　　　　　　　　　　　 2　　  3

　　　　　　　　　　　　　  /   \　 /   \

   　　　　　　　　　　　　4     5  6    7

       我们使用一个栈来解决问题。步骤如下：

　　　　一，我们将根节点1入栈，如果有左孩子，依次入栈，那么入栈顺序为：1，2，4。由于4的左子树为空，停止入栈，此时栈为{1，2，4}。

　　　　二，此时将4出栈，并遍历4，由于4也没有右孩子，那么根据中序遍历的规则，我们显然应该继续遍历4的父亲2，情况是这样。所以我们继续将2出栈并遍历2，2存在右孩子，将5入栈，此时栈为{1，5}。

　　　　三，5没有孩子，则将5出栈并遍历5，这也符合中序遍历的规则。此时栈为{1}。

　　　　四，1有右孩子，则将1出栈并遍历1，然后将右孩子3入栈，并继续以上三个步骤即可。

　　　　栈的变化过程：{1}->{1,2}->{1,2,4}->{1,2}->{1}->{1,5}->{1}->{}->{3}->{3,6}->{3}->{}->{7}->{}。
        """
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
        return res

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


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    print(Solution().inorder_non_recursive(node1))