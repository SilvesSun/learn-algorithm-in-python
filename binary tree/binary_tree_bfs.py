def level_order(root):
    if root is None: return []
    level_list = [root]
    res = []
    while level_list:
        root = level_list.pop()
        res.append(root.val)
        if root.left_child is not None:
            level_list.append(root.left_child)
        if root.right_child is not None:
            level_list.append(root.right_child)