from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 假设每一种面额的硬币有无限个. 说明是一个完全背包问题
        if amount == 0:
            return 1
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # 容量为0时, 什么都不选, 有一种方法
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))
