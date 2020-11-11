# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.convert(pRootOfTree.left)
        if self.listHead is None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree

        self.convert(pRootOfTree.right)
        return self.listHead
