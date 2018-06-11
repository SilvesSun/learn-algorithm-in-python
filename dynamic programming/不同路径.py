# coding:utf-8


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for col in range(n + 1)] for row in range(m + 1)]
        dp[1][1] = 1
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if dp[row - 1][col]:
                    dp[row][col] += dp[row - 1][col]
                if dp[row][col - 1]:
                    dp[row][col] += dp[row][col - 1]
        return dp[m][n]


s = Solution()
print(s.uniquePaths(7, 3))
