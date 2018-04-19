# coding:utf-8


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_row = len(grid)
        len_col = len(grid[0])
        dp = [[0 for col in range(len_col)] for row in range(len_row)]
        dp[0][0] = grid[0][0]

        for i in range(1, len_row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, len_col):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, len_row):
            for j in range(1, len_col):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[len_row-1][len_col-1]