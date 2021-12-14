# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
#  在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表
# 示如果要学习课程 ai 则 必须 先学习课程 bi 。
#
#
#  例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
#
#
#  请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
#  示例 1：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
#  示例 2：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
#
#  提示：
#
#
#  1 <= numCourses <= 105
#  0 <= prerequisites.length <= 5000
#  prerequisites[i].length == 2
#  0 <= ai, bi < numCourses
#  prerequisites[i] 中的所有课程对 互不相同
#
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序
#  👍 1046 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        邻接表实现
        """
        n = len(prerequisites)
        if not n:
            return True

        # 1.统计入度
        in_degree = [0 for _ in range(numCourses)]
        # 邻接表，使用散列表是为了去重
        adj = [set() for _ in range(numCourses)]
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0, 1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        for second, first in prerequisites:
            in_degree[second] += 1
            adj[first].add(second)

        # 2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        counter = 0
        while queue:
            top = queue.popleft()
            counter += 1
            # 3：把这个结点的所有后继结点的入度减去 1，如果发现入度为 0 ，就马上添加到队列中
            for successor in adj[top]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    queue.append(successor)
        return counter == numCourses

    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        说明：深度优先遍历的思路有 2 个。
        1. 首先检测是否存在环，然后使用「深度优先遍历」，在「后序」的部分把课程添加到结果集，然后再逆序，就是「拓扑排序」的结果；
        2. 在深度优先遍历的过程中，设置个别有特殊意义的变量，通过这些变量得到「拓扑排序」的结果(下面提供了参考代码)
        """
        clen = len(prerequisites)
        if not clen:
            return True

        # 深度优先遍历，判断结点是否访问过
        # 这里要设置 3 个状态
        # 0 就对应 False ，表示结点没有访问过
        # 1 就对应 True ，表示结点已经访问过，在深度优先遍历结束以后才置为 1
        # 2 表示当前正在遍历的结点，如果在深度优先遍历的过程中，有遇到状态为 2 的结点，就表示这个图中存在环
        visited = [0 for _ in range(numCourses)]
        # 逆邻接表，存的是每个结点的前驱结点的集合
        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # 1 在前，0 在后
        inverse_adj = [set() for _ in range(numCourses)]
        for second, first in prerequisites:
            inverse_adj[second].add(first)

        for i in range(numCourses):
            # 在遍历的过程中，如果发现有环，就退出
            if self.dfs(i, inverse_adj, visited):
                return False
        return True

    def dfs(self, vertex, inverse_adj, visited):
        if visited[vertex] == 2:
            # 遇到环
            return True
        if visited[vertex] == 1:
            return False
        visited[vertex] = 2
        for pre in inverse_adj[vertex]:
            if self.dfs(pre, inverse_adj, visited):
                return True
        visited[vertex] = 1
        return False


if __name__ == '__main__':
    print(Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))