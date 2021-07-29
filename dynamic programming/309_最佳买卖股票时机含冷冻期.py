class Solution:
    def max_profit(self, prices):
        # 状态: 持有股票, 卖出股票(2天前卖出股票, 当天卖出), 冷冻期
        n = len(prices)
        dp = [[0] * 4 for i in range(n)]
        # dp[i][0] 表示买入股票, 分
        # 1. 前一天就是持有股票状态, dp[i][0] = dp[i-1][0]
        # 2. 当天买入, 前一天为冷冻期 dp[i][0] = dp[i-1][3] - prices[i]
        # 3. 当天买入, 前一天为卖出状态 dp[i][0] = dp[i-1][2] - prices[i]
        # dp[i][0] = max(dp[i-1][0], max(dp[i-1][3] - prices[i], dp[i-1][2] - prices[i]))

        # dp[i][1] 保持股票卖出状态
        # 1. 前一天就是卖出状态, 且不为冷冻期 dp[i][1]= dp[i-1][1]
        # 2. 前一天为冷冻期, dp[i][1] = dp[i-1][3]
        # dp[i][1] = max(dp[i-1][1], dp[i-1][3])

        # dp[i][2] 当天股票可卖出, 那么手上一定要有股票 dp[i][2] = dp[i-1][0] + prices[i]

        # dp[i][3] 处于冷冻期, 那么一定是前一天卖出了股票 dp[i][3] = dp[i-1][2]
        if not prices: return 0
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]))
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]
        return max(dp[n - 1][3], max(dp[n - 1][1], dp[n - 1][2]))


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    print(Solution().max_profit(prices))
