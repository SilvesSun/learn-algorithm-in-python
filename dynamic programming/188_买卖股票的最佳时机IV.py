from pprint import pprint
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 状态总数为 2k + 1, 设计数为买入, 偶数为卖出
        # 0,1,2,3,4...
        # 无操作, 买入一次, 卖出一次, 买入二次, 卖出二次...
        if not prices: return 0
        n = len(prices)
        dp = [[0] * (2 * k + 1) for _ in range(n)]
        for i in range(1, 2 * k, 2):
            dp[0][i] = -prices[0]
        for i in range(1, n):
            for j in range(0, 2 * k - 1, 2):
                dp[i][j + 1] = max(dp[i - 1][j] - prices[i], dp[i - 1][j + 1])
                dp[i][j + 2] = max(dp[i - 1][j + 1] + prices[i], dp[i - 1][j + 2])
        return dp[n - 1][2 * k]


if __name__ == '__main__':
    k = 2
    prices = [3,2,6,5,0,3]
    print(Solution().maxProfit(k, prices))