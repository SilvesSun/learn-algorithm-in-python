# 现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui,
# vi] 表示顶点 ui 和 vi 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。
#
#  返回图中 最短 环的长度。如果不存在环，则返回 -1 。
#
#  环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。
#
#
#
#  示例 1：
#  输入：n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
# 输出：3
# 解释：长度最小的循环是：0 -> 1 -> 2 -> 0
#
#
#  示例 2：
#  输入：n = 4, edges = [[0,1],[0,2]]
# 输出：-1
# 解释：图中不存在循环
#
#
#
#
#  提示：
#
#
#  2 <= n <= 1000
#  1 <= edges.length <= 1000
#  edges[i].length == 2
#  0 <= ui, vi < n
#  ui != vi
#  不存在重复的边
#
#
#  Related Topics 广度优先搜索 图 👍 38 👎 0
import heapq


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findShortestCycle_dijkstra(self, n: int, edges: List[List[int]]) -> int:
        # 基于 dijkstra 算法，每次遍历到一个节点，就把这个节点加入到最短路径中，如果遍历到一个已经在最短路径中的节点，那么就更新最短路径
        g = [[] for _ in range(n)]
        # 构建邻接表
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dijkstra(graph, start, end, ignore_edge):
            n = len(graph)
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                cur_dist, u = heapq.heappop(heap)
                if cur_dist > dist[u]:
                    continue

                if u == end:
                    return cur_dist
                for v in graph[u]:
                    if (u, v) == ignore_edge or (v, u) == ignore_edge:
                        # 跳过忽略的边
                        continue

                    if cur_dist + 1 < dist[v]:
                        dist[v] = cur_dist + 1
                        heapq.heappush(heap, (dist[v], v))
            return float('inf')

        ans = float('inf')
        for u, v in edges:
            dist = dijkstra(g, u, v, (u, v))
            # 如果dist != float('inf')，说明存在环
            if dist != float('inf'):
                ans = min(ans, dist + 1)
        return ans if ans != float('inf') else -1

    def findShortestCycle_bfs(self, n: int, edges: List[List[int]]) -> int:
        from math import inf
        from collections import deque
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图


        def bfs(start: int) -> int:
            ans = inf
            dis = [-1] * n  # dis[i] 表示从 start 到 i 的最短路长度
            dis[start] = 0
            q = deque([(start, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:  # 第一次遇到
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:  # 第二次遇到
                        ans = min(ans, dis[x] + dis[y] + 1)
            return ans

        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1



# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.findShortestCycle_bfs(7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]))