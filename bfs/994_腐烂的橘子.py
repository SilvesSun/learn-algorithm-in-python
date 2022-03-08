# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
#
#  值 0 代表空单元格；
#  值 1 代表新鲜橘子；
#  值 2 代表腐烂的橘子。
#
#
#  每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
#  返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
#
#
#
#  示例 1：
#
#
#
#
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#
#
#  示例 2：
#
#
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#
#
#  示例 3：
#
#
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 10
#  grid[i][j] 仅为 0、1 或 2
#
#  Related Topics 广度优先搜索 数组 矩阵 👍 512 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rnd = 0
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # all rotten orange
        row = len(grid)
        col = len(grid[0])
        rotten = [(i, j, rnd) for j in range(col) for i in range(row) if grid[i][j] == 2]
        while rotten:
            i, j, rnd = rotten.pop(0)
            # bfs
            for di, dj in directs:
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i+di][j+dj] == 1:
                    grid[i+di][j+dj] = 2
                    rotten.append((i+di, j+dj, rnd + 1))
        for row in grid:
            if 1 in row: return -1
        return rnd
# leetcode submit region end(Prohibit modification and deletion)
