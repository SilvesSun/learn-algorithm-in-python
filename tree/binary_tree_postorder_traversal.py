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