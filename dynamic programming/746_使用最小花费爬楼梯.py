from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 定义dp, 到达第i 个台阶需要的花费为dp[i]
        dp = [float('NaN')] * len(cost)
        # 和爬楼梯一样, 有两种方式到达楼梯i, 要求最小的消费, 所以 dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(int(dp[-1]), int(dp[-2]))


if __name__ == '__main__':

    print(Solution().minCostClimbingStairs([10, 15, 20]))