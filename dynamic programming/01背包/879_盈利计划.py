"""
集团里有 n 名员工，他们可以完成各种各样的工作创造利润。

 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。

 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。

 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。

 示例 1：

输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
输出：2
解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。

 示例 2：

输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
输出：7
解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。




 提示：


 1 <= n <= 100
 0 <= minProfit <= 100
 1 <= group.length <= 100
 1 <= group[i] <= 100
 profit.length == group.length
 0 <= profit[i] <= 100


 Related Topics 数组 动态规划 👍 334 👎 0

"""
from functools import cache
from pprint import pprint
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # 定义 f(i, j, k) 表示从前 i 个工作中选择，使用 n 名员工，且至少产生 k 利润的方案数
        mod = 10 ** 9 + 7

        @cache
        def f(i, j, k):
            # 如果 i = 0 或者 j == 0, 返回1, 即不做任何工作存在一个方案
            if i == len(group) or n == 0:
                return 1 if k == 0 else 0

            # 如果利润要求为负数（k < 0），则可以忽略，因为已经满足了利润要求
            if k < 0:
                return 0

            # 不选择第i个工作
            res = f(i + 1, j, k)
            # 选择第i个工作
            if n >= group[i]:
                res += f(i + 1, j - group[i], max(0, k - profit[i]))
            return res % mod

        return f(0, n, minProfit)

    def profitableSchemesDy(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 10 ** 9 + 7
        # dp[i][j][k] 表示从前 i 个工作中选择，使用 j 名员工，且至少产生 k 利润的方案数
        dp = [[[0 for _ in range(minProfit + 1)] for _ in range(n + 1)] for _ in range(len(group) + 1)]
        dp[0][0][0] = 1
        for i in range(1, len(group) + 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= group[i - 1]:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j - group[i - 1]][max(0, k - profit[i - 1])]) % mod
        # 最终结果为所有可能人数下（0 ≤ j ≤ n），满足 dp[len(group)][j][minProfit] 的总和
        total = 0
        for j in range(n + 1):
            total += dp[-1][j][minProfit]
            total %= mod
        return total


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().profitableSchemesDy(n=5, minProfit=3, group=[2, 2], profit=[2, 3]))
