# 你现在手里有一份大小为
#  n x n 的 网格 grid，上面的每个 单元格 都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地。
#
#  请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的，并返回该距离。如果网格上只有陆地或者海洋，请返回 -1。
#
#  我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个单元格之间的距离是 |x0 -
# x1| + |y0 - y1| 。
#
#
#
#  示例 1：
#
#
#
#
# 输入：grid = [[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释：
# 海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。
#
#
#  示例 2：
#
#
#
#
# 输入：grid = [[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释：
# 海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。
#
#
#
#
#  提示：
#
#
#
#
#
#  n == grid.length
#  n == grid[i].length
#  1 <= n <= 100
#  grid[i][j] 不是 0 就是 1
#
#
#  Related Topics 广度优先搜索 数组 动态规划 矩阵 👍 416 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        # 多源bfs
        n = len(grid)
        q = deque()

        # 首先找到所有的初始岛屿
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        if not q or len(q) == n * n:
            return -1

        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            step += 1

        return step - 1

# leetcode submit region end(Prohibit modification and deletion)
