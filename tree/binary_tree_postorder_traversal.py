# coding:utf-8


class Solution:
    # @param root, a tree node
    # @return a list of integers
    # recursive

    def recursive_postorder(self, root, list):
        if not root:
            return None
        if root:
            self.recursive_postorder(root.left, list)
            self.recursive_postorder(root.right, list)
            list.append(root.val)

    def iterative_postorder(self, root, list):
        """
        http://www.cnblogs.com/zuoyuan/p/3720846.html
        解题思路：这道题的迭代求解比先序遍历和后序遍历要麻烦一些。假设一棵树是这样的：

　　　　　　　　　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　　　　　　　　　/　　\

　　　　　　　　　　　　　　　　　　　　　　2　　　　3

　　　　　　　　　　　　　　　　　　　　　　　　　　/　\

　　　　　　　　　　　　　　　　　　　　　　　　　 4　　5

　　　　　使用一个栈。分几个步骤：

　　　　　一，将根节点入栈，并将根节点的孩子入栈，入栈顺序为：先入右孩子，再入左孩子，顺序不能错。因为这样在弹栈时的顺序就是后序遍历的顺序了。
        如果左孩子还有左孩子或者右孩子，那么继续按先右后左的顺序入栈。那么上面这棵树开始的入栈顺序是：1，3，2。由于2不存在左右孩子，停止入栈。

　　　　   二，由于2没有左右孩子，遍历2并将2弹出，同时使用prev记录下2这个节点。

　　　　   三，2出栈后，栈为{1，3}，此时3在栈顶，由于3存在左右孩子，按顺序入栈，此时栈为{1，3，5，4}。

　　　　   四，将4和5遍历并出栈，此时prev指向5，栈为{1，3}。prev的作用是什么呢？用来判断prev是否为栈顶元素的孩子，如果是，则说明子树的孩子已经遍历完成，
        需要遍历树根了。以上树为例：4和5出栈后，prev指向5，而5是栈顶元素3的孩子，说明孩子已经遍历完毕，则遍历3然后弹出3即可，即完成了子树{3，4，5}的后序遍历。

　　　　   五，此时栈为{1}，为树根，而左右子树都遍历完了，最后遍历树根并弹出即可。
        :param root:
        :param list:
        :return:
        """
        stack = []
        pre = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[len(stack) - 1]
                if (curr.left is None and curr.right is None) or (pre and (pre == curr.left or pre == curr.right )):
                    list.append(curr.val)
                    stack.pop()
                    pre = curr
                else:
                    if curr.right: stack.append(curr.right)
                    if curr.left: stack.append(curr.left)
        return list

    def postorder_traversal(self, root):
        list = []
        self.iterative_postorder(root, list)
        return list