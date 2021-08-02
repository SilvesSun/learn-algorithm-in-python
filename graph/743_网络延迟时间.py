class Solution:
    def network_delay_time(self, times, n, k):
        """
        本题需要用到单源最短路径算法 \texttt{Dijkstra}Dijkstra，现在让我们回顾该算法，其主要思想是贪心。

        将所有节点分成两类：已确定从起点到当前点的最短路长度的节点，以及未确定从起点到当前点的最短路长度的节点（下面简称「未确定节点」和「已确定节点」）。

        每次从「未确定节点」中取一个与起点距离最短的点，将它归类为「已确定节点」，并用它「更新」从起点到其他所有「未确定节点」的距离。直到所有点都被归类为「已确定节点」。

        用节点 AA「更新」节点 BB 的意思是，用起点到节点 AA 的最短路长度加上从节点 AA 到节点 BB 的边的长度，去比较起点到节点 BB 的最短路长度，如果前者小于后者，就用前者更新后者。这种操作也被叫做「松弛」。

        这里暗含的信息是：每次选择「未确定节点」时，起点到它的最短路径的长度可以被确定。

        可以这样理解，因为我们已经用了每一个「已确定节点」更新过了当前节点，无需再次更新（因为一个点不能多次到达）。而当前节点已经是所有「未确定节点」中与起点距离最短的点，不可能被其它「未确定节点」更新。所以当前节点可以被归类为「已确定节点」。

        """
        # 输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        # 输出：2
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = [False] * n
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1