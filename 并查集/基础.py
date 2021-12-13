class UF:
    def __init__(self, count: int):
        self.count = count
        # parent[i]表示的含义为，键值为i的节点，它的直接父节点为parent[i]
        self.parent = [''] * count
        # 最初每棵树只有一个节点
        # 重量应该初始化
        self.size = [1] * count
        for i in range(count):
            self.parent[i] = i

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
            # // 小树接到大树下面，较平衡
        if self.size[root_p] > self.size[root_q]:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        else:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        self.count -= 1

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    def connect(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q

    def count(self):
        return self.count