# 给你一个整数 n 和一个二维整数数组 queries。
#
#  有 n 个城市，编号从 0 到 n - 1。初始时，每个城市 i 都有一条单向道路通往城市 i + 1（ 0 <= i < n - 1）。
#
#  queries[i] = [ui, vi] 表示新建一条从城市 ui 到城市 vi 的单向道路。每次查询后，你需要找到从城市 0 到城市 n - 1 的最
# 短路径的长度。
#
#  返回一个数组 answer，对于范围 [0, queries.length - 1] 中的每个 i，answer[i] 是处理完前 i + 1 个查询后，
# 从城市 0 到城市 n - 1 的最短路径的长度。
#
#
#
#  示例 1：
#
#
#  输入： n = 5, queries = [[2, 4], [0, 2], [0, 4]]
#
#
#  输出： [3, 2, 1]
#
#  解释：
#
#
#
#  新增一条从 2 到 4 的道路后，从 0 到 4 的最短路径长度为 3。
#
#
#
#  新增一条从 0 到 2 的道路后，从 0 到 4 的最短路径长度为 2。
#
#
#
#  新增一条从 0 到 4 的道路后，从 0 到 4 的最短路径长度为 1。
#
#  示例 2：
#
#
#  输入： n = 4, queries = [[0, 3], [0, 2]]
#
#
#  输出： [1, 1]
#
#  解释：
#
#
#
#  新增一条从 0 到 3 的道路后，从 0 到 3 的最短路径长度为 1。
#
#
#
#  新增一条从 0 到 2 的道路后，从 0 到 3 的最短路径长度仍为 1。
#
#
#
#  提示：
#
#
#  3 <= n <= 500
#  1 <= queries.length <= 500
#  queries[i].length == 2
#  0 <= queries[i][0] < queries[i][1] < n
#  1 < queries[i][1] - queries[i][0]
#  查询中没有重复的道路。
#
#
#  Related Topics 广度优先搜索 图 数组 👍 78 👎 0
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        # grid[i] 表示从城市i出发可以到达的城市
        grid = [[] for _ in range(n)]
        for i in range(n - 1):
            grid[i].append(i + 1)
        ans = []

        def bfs():
            queue = deque([0])
            visited = [False] * n
            distance = 0
            while queue:
                # 遍历当前队列所有节点，保证层序遍历，每次distance加1表示距离加1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    # 如果当前弹出的是目标城市 n-1，直接返回距离即为最短路径长度
                    if node == n - 1:
                        return distance
                    # 如果当前节点已经被访问过，则跳过
                    if visited[node]:
                        continue

                    visited[node] = True
                    # 遍历当前节点的邻居节点，加入队列
                    for neighbor in grid[node]:
                        queue.append(neighbor)
                distance += 1
            # 如果队列为空，说明没有到达目标城市，返回-1
            return -1

        for u, v in queries:
            grid[u].append(v)
            ans.append(bfs())

        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    s = Solution()
    res = s.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]])
    print(res)
