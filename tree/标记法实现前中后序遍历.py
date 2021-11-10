from tree.util import TreeNode


class Solution:
    def preorder(self, root):
        res = []
        stack = []
        if root: stack.append(root)
        while stack:
            node = stack[-1]
            if node:
                stack.pop()
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
                # root节点
                stack.append(node)
                stack.append(None)  # 标记前一个节点已处理
            else:
                # 遇到一个空节点, 下一个为root
                stack.pop()
                res.append(stack.pop().val)
        return res

    def inorder(self, root):
        res = []
        stack = []
        if root: stack.append(root)
        while stack:
            node = stack[-1]
            if node:
                stack.pop()
                if node.right: stack.append(node.right)
                # root节点
                stack.append(node)
                stack.append(None)  # 标记前一个节点已处理
                if node.left: stack.append(node.left)
            else:
                # 遇到一个空节点, 下一个为root
                stack.pop()
                res.append(stack.pop().val)
        return res

    def postorder(self, root):
        res = []
        stack = []
        if root: stack.append(root)
        while stack:
            node = stack[-1]
            if node:
                stack.pop()
                # root节点
                stack.append(node)
                stack.append(None)  # 标记前一个节点已处理
                if node.right: stack.append(node.right)
                if node.left: stack.append(node.left)
            else:
                # 遇到一个空节点, 下一个为root
                stack.pop()
                res.append(stack.pop().val)
        return res


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

    s = Solution()
    print(s.preorder(node1), s.inorder(node1), s.postorder(node1))