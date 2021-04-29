class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 递归
        # time limit exceeded
        def dp(i, j):
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(len(text1) - 1, len(text2) - 1)

    def longestCommonSubsequence2(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
