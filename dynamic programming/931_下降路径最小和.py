# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
#
#  下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第
# 一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1
# , col + 1) 。
#
#
#
#  示例 1：
#
#
#
#
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：如图所示，为和最小的两条下降路径
#
#
#  示例 2：
#
#
#
#
# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：如图所示，为和最小的下降路径
#
#
#
#
#  提示：
#
#
#  n == matrix.length == matrix[i].length
#  1 <= n <= 100
#  -100 <= matrix[i][j] <= 100
#
#
#  Related Topics 数组 动态规划 矩阵 👍 393 👎 0
import math
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # https://leetcode.cn/problems/minimum-falling-path-sum/solutions/2341851/cong-di-gui-dao-di-tui-jiao-ni-yi-bu-bu-2cwkb/
        # 用 f[i][j] 表示到达 matrix[i][j] 的下降路径最小和
        # f[i][j] = min(f[i-1][j-1], f[i-1][j], f[i-1]j + 1) + matrix[i][j]
        n = len(matrix)
        arr = [[math.inf] * (n + 1) for _ in range(n)]
        # 初始化
        for i in range(1, n+1):
            arr[0][i] = matrix[0][i-1]
        for i in range(1, n):
            for j in range(1, n+1):
                if j == n:
                    arr[i][j] = min(arr[i - 1][j - 1], arr[i - 1][j]) + matrix[i][j-1]
                else:
                    arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1]) + matrix[i][j-1]
        return min(arr[n-1])


if __name__ == '__main__':
    s = Solution()
    print(s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
