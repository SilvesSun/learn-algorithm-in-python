# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1：
#
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 300
#  grid[i][j] 的值为 '0' 或 '1'
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 1330 👎 0


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

    def dfs(self, grid, i, j):
        if not (0 <= i <= len(grid) and 0 <= j <= len(grid[0])):
            # i, j 已超出边界
            return
        if grid[i][j] == '0':
            # 遇到岛的边界
            return
        grid[i][j] = '0'  # 原地修改, 避免重复遍历
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)


if __name__ == '__main__':
    print(Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
