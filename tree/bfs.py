def bfs(root):
    res = []
    # 如果根节点为空，则返回空列表
    if root is None:
        return res
    # 模拟一个队列储存节点
    q = []
    # 首先将根节点入队
    q.append(root)
    # 列表为空时，循环终止
    while len(q) != 0:
        length = len(q)
        for i in range(length):
            # 将同层节点依次出队
            r = q.pop(0)
            if r.left is not None:
                # 非空左孩子入队
                q.append(r.left)
            if r.right is not None:
                # 非空右孩子入队
                q.append(r.right)
            res.append(r.value)
    return res



