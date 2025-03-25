"""
给你一个 n x n 整数矩阵 grid ，请你返回 非零偏移下降路径 数字和的最小值。

 非零偏移下降路径 定义为：从 grid 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。



 示例 1：




输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
输出：13
解释：
所有非零偏移下降路径包括：
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。


 示例 2：


输入：grid = [[7]]
输出：7




 提示：


 n == grid.length == grid[i].length
 1 <= n <= 200
 -99 <= grid[i][j] <= 99


 Related Topics 数组 动态规划 矩阵 👍 216 👎 0

"""
import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        # f[i][j] = min(f[i-1][0...j-1, j+1, n]) + grid[i][j]
        dp[0] = grid[0]
        for i in range(1, n):
            for j in range(n):
                # 上一层中不等于当前列的所有路径中最小值
                min_value = float('inf')
                for k in range(n):
                    if k != j:
                        min_value = min(min_value, dp[i - 1][k])
                dp[i][j] = min_value + grid[i][j]
        return min(dp[n-1])

