class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s[::-1]
        # 转换为求最长公共子序列
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]
