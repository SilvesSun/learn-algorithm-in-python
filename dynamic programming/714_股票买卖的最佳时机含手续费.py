from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0] 表示第i天持有股票所省最多现⾦。
        # dp[i][1] 表示第i天不持有股票所得最多现⾦
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = -prices[0]

        # 持有股票
        # i-1之前就有股票和当天买入股票
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])

        # 不持有股票
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
        return max(dp[n - 1][0], dp[n - 1][1])
