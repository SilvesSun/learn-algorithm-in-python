class Solution(object):
    def coin_change(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        - base case: amount is 0
        - state: 原问题和子问题中的变量, 此问题的变量为目标金额
        - 确定选择, 导致状态变化的行为, 这里是选择一个硬币导致目标金额的变更
        - 确定dp函数: 输入一个目标金额, 返回凑出目标金额的最小硬币数量
        def dp(n):
            for coin in coins:
                res = min(res, 1 + dp(n - coin))
            return res
        暴力解法
        """

        def dp(n):
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1: continue
                res = min(res, 1 + sub)
            return res if res != float('INF') else -1

        return dp(amount)

    def coin_change2(self, coins, amount):
        # 备忘录
        memo = {}

        def dp(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1: continue
                res = min(res, 1 + sub)
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)

    def coin_change3(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 5
    s = Solution()
    print(s.coin_change(coins, amount))
