class Solution:
    def maximalSquare(self, matrix):
        row = len(matrix)
        if not row: return 0
        col = len(matrix[0])
        if not col: return 0

        dp = [[0] * col for _ in range(row)]
        dp[0][0] = 0
        max_side = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
        return max_side ** 2


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(Solution().maximalSquare(matrix))
