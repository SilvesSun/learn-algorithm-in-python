"""
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365
的整数。

 火车票有 三种不同的销售方式 ：


 一张 为期一天 的通行证售价为 costs[0] 美元；
 一张 为期七天 的通行证售价为 costs[1] 美元；
 一张 为期三十天 的通行证售价为 costs[2] 美元。


 通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张 为期 7 天 的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第
 5 天、第 6 天、第 7 天和第 8 天。

 返回 你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费 。



 示例 1：


输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。


 示例 2：


输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
输出：17
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。
你总共花了 $17，并完成了你计划的每一天旅行。




 提示：


 1 <= days.length <= 365
 1 <= days[i] <= 365
 days 按顺序严格递增
 costs.length == 3
 1 <= costs[i] <= 1000


 Related Topics 数组 动态规划 👍 683 👎 0

"""
from functools import cache
from typing import List

"""
寻找子问题:
假设第100天是旅行的最后一天, 那么到达最后一天可以有三种方式
1. 购买1天的通行证, 那么需要解决前99天的最小花费
2. 购买7天的通行证, 那么需要解决前93天的最小花费 
3. 购买30天的通行证, 那么需要解决前70天的最小花费

ps: 动态规划有「选或不选」和「枚举选哪个」两种基本思考方式。在做题时，可根据题目要求，选择适合题目的一种来思考。本题用到的是「枚举选哪个」

定义dfs(i) 表示前i天旅行的最小花费

如果第i天不在 days 中, 那么第i天不需要买票, 那么 dfs(i) = dfs(i-1), 如果在 days 中, 则 
dfs(i) = min(dfs(i-1) + costs[0], dfs(i-7) + costs[1], dfs(i-30) + costs[2])


"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        days_set = set(days)

        @cache
        def dfs(i):
            if i <= 0:
                return 0
            if i not in days_set:
                return dfs(i - 1)
            return min(dfs(i - 1) + costs[0], dfs(i - 7) + costs[1], dfs(i - 30) + costs[2])

        return dfs(last_day)

    def mincostTickets2(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        days_set = set(days)
        dp = [float('inf') for _ in range(last_day + 1)]

        dp[0] = 0
        for i in range(1, last_day + 1):
            if i not in days_set:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(i-1, 0)] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
