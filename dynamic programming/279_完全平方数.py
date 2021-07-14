class Solution:
    def num_squares(self, n):
        # 完全平⽅数就是物品（可以⽆限件使⽤），凑个正整数n就是背包，问凑满这个背包最少有多少物品？
        # dp定义: 和为i的完全平⽅数的最少数量为dp[i]
        dp = [n] * (n + 1)
        dp[0] = 0
        # 首先遍历背包
        for i in range(0, n+1):
            # 物品
            for j in range(1, i+1):
                if j * j <= i:
                    dp[i] = min(dp[i - j * j] + 1, dp[i])
        return dp[n]


if __name__ == '__main__':
    Solution().num_squares(12)