def dfs(root):
    if root is None:
        return
    print(root.value)
    root.visit = True
    for node in root.adjacent:
        if not node.visit:
            dfs(node)
