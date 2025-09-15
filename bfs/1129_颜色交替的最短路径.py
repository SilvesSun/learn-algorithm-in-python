# 给定一个整数 n，即有向图中的节点数，其中节点标记为 0 到 n - 1。图中的每条边为红色或者蓝色，并且可能存在自环或平行边。
#
#  给定两个数组 redEdges 和 blueEdges，其中：
#
#
#  redEdges[i] = [ai, bi] 表示图中存在一条从节点 ai 到节点 bi 的红色有向边，
#  blueEdges[j] = [uj, vj] 表示图中存在一条从节点 uj 到节点 vj 的蓝色有向边。
#
#
#  返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，
# 那么 answer[x] = -1。
#
#
#
#  示例 1：
#
#
# 输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# 输出：[0,1,-1]
#
#
#  示例 2：
#
#
# 输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# 输出：[0,1,-1]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 100
#  0 <= redEdges.length, blueEdges.length <= 400
#  redEdges[i].length == blueEdges[j].length == 2
#  0 <= ai, bi, uj, vj < n
#
#
#  Related Topics 广度优先搜索 图 👍 339 👎 0
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        grid = [[] for _ in range(n)]
        # 源节点0对应列表中的第0个元素，该元素中的第1个值表示目标节点，第二个值表示边的颜色
        for edge in redEdges:
            grid[edge[0]].append((edge[1], "r"))
        for edge in blueEdges:
            grid[edge[0]].append((edge[1], "b"))
        ans = [-1] * n
        q = deque([(0, "r"), (0, "b")])

        level = 0
        visited = {(0, "r"), (0, "b")}
        while q:
            size = len(q)
            for _ in range(size):
                node, color = q.popleft()
                if ans[node] == -1:
                    ans[node] = level
                # 遍历当前节点的所有邻居节点
                for neighbor, c in grid[node]:
                    # 如果邻居节点的颜色与当前节点的颜色不同，且该邻居节点未被访问过，则将其加入队列, 标准的bfs过程
                    if c != color and (neighbor, c) not in visited:
                        visited.add((neighbor, c))
                        q.append((neighbor, c))
            level += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.shortestAlternatingPaths(n=3, redEdges=[[0, 1], [1, 2]], blueEdges=[]))