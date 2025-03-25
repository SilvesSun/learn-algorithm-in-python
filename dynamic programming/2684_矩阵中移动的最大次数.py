# 给你一个下标从 0 开始、大小为 m x n 的矩阵 grid ，矩阵由若干 正 整数组成。
#
#  你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 grid ：
#
#
#  从单元格 (row, col) 可以移动到 (row - 1, col + 1)、(row, col + 1) 和 (row + 1, col + 1) 三个
# 单元格中任一满足值 严格 大于当前单元格的单元格。
#
#
#  返回你在矩阵中能够 移动 的 最大 次数。
#
#
#
#  示例 1：
#  输入：grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# 输出：3
# 解释：可以从单元格 (0, 0) 开始并且按下面的路径移动：
# - (0, 0) -> (0, 1).
# - (0, 1) -> (1, 2).
# - (1, 2) -> (2, 3).
# 可以证明这是能够移动的最大次数。
#
#  示例 2：
#
#
# 输入：grid = [[3,2,4],[2,1,9],[1,1,7]]
# 输出：0
# 解释：从第一列的任一单元格开始都无法移动。
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  2 <= m, n <= 1000
#  4 <= m * n <= 10⁵
#  1 <= grid[i][j] <= 10⁶
#
#
#  Related Topics 数组 动态规划 矩阵 👍 76 👎 0
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # 当前单元格可以移动到其右上方、正右方以及右下方三个位置中严格大于其的单元格。那么换个角度想，一个单元格可以从其左上方、正左方以及左下方的单元格转移过来。
        # 一旦单元格满足了大于其左侧三个单元格位置的，那么能够到达当前单元格就取决于能否到达其之前位置的单元格是否能够到达。这就变成拆分子问题了，
        # 记 canMove[i][j] 表示能够到达单元格 (i, j)，那么状态转移方程即为：canMove[i][j] |= canMove[i-p][j - 1] && (grid[i][j] > grid[i-p][j-1])，p=-1,0,1。
        # 并且只要能到达单元格 (i, j) ，就说明能到达索引 j 列，最大移动次数至少为 j。
        # 初始条件首列一定是可达的， canMove[i][0] = true
        m = len(grid)
        n = len(grid[0])
        can_move = [[0 for _ in range(n)] for _ in range(m)]
        ret = 0
        for j in range(1, n):
            for i in range(n):
                for p in [-1, 0, 1]:
                    if i + p < 0 or i + p >= m:
                        continue
                    if grid[i][j] > grid[i + p][j - 1] and (j == 1 or can_move[i + p][j - 1]):
                        can_move[i][j] = 1
                        ret = j
                        break
        return ret
