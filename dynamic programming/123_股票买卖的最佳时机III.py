from pprint import pprint
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 状态列表
        # 0,1,2,3,4
        # 无操作, 买入一次, 卖出一次, 买入二次, 卖出二次
        dp = [[0] * 5 for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][1] + prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][2] - prices[i], dp[i-1][3])
            dp[i][4] = max(dp[i-1][3] + prices[i], dp[i-1][4])
        pprint(dp)
        return dp[-1][4]


if __name__ == '__main__':
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(Solution().maxProfit(prices))
