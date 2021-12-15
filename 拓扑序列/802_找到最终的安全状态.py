# 在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。
#
#  对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。
#
#  返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。
#
#  该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，
# 满足 (i, j) 是图的一条有向边。
#
#
#
#
#
#  示例 1：
#
#
# 输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# 输出：[2,4,5,6]
# 解释：示意图如上。
#
#
#  示例 2：
#
#
# 输入：graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# 输出：[4]
#
#
#
#
#  提示：
#
#
#  n == graph.length
#  1 <= n <= 104
#  0 <= graph[i].length <= n
#  graph[i] 按严格递增顺序排列。
#  图中可能包含自环。
#  图中边的数目在范围 [1, 4 * 104] 内。
#
#
#
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序
#  👍 286 👎 0
from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        若一个节点没有出边，则该节点是安全的；若一个节点出边相连的点都是安全的，则该节点也是安全的。

        将图中所有边反向，得到一个反图，然后在反图上运行拓扑排序
        具体来说，首先得到反图 rg 及其入度数组 inDeg。将所有入度为 0 的点加入队列，然后不断取出队首元素，将其出边相连的点的入度减一，
        若该点入度减一后为 0，则将该点加入队列，如此循环直至队列为空。循环结束后，所有入度为 0 的节点均为安全的。我们遍历入度数组，并将入度为 0 的点加入答案列表

        """
        rg = [[] for _ in graph]
        for j, i in enumerate(graph):
            for inode in i:
                rg[inode].append(j)
        in_deg = [len(ys) for ys in graph]

        q = deque([i for i, d in enumerate(in_deg) if d == 0])
        while q:
            for x in rg[q.popleft()]:
                in_deg[x] -= 1
                if in_deg[x] == 0:
                    q.append(x)

        return [i for i, d in enumerate(in_deg) if d == 0]


if __name__ == '__main__':
    print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
