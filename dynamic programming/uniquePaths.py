class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # dp[i][j]表示到达第i行第j列有几种方法，初始为1
        dp = [[1] * n for _ in range(m)]
        dp[0][0] = 1
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[m-1][n-1]


s= Solution()
print(s.uniquePaths(7, 3))
