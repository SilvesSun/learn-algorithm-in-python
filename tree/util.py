from ppbtree import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"node: {self.val}"


def array_to_tree(array, index):
    if not index < len(array):
        return
    value = array[index]
    if value is None:
        return None
    root = TreeNode(value)
    root.left = array_to_tree(array, 2 * index + 1)
    root.right = array_to_tree(array, 2 * index + 2)
    return root


if __name__ == '__main__':
    array = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    tree = array_to_tree(array, 0)
    print_tree(tree)
