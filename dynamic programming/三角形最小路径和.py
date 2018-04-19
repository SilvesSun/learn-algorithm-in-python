# coding:utf-8
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 状态转移方程
        # dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + t[i][j]

        max_len = len(triangle)
        dp = [[0 for j in range(i + 1)] for i in range(max_len)]
        dp[0][0] = triangle[0][0]
        if max_len < 0:
            return
        if max_len == 1:
            return triangle[0][0]

        for i in range(1, max_len):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(2, max_len):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[max_len-1])


s = Solution()
triangle = [[-1],[3,2],[-3,-1,-2]]
print(s.minimumTotal(triangle))
