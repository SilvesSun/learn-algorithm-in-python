# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。
#
#  给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
#
#  开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。
#
#  如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。
#
#
#
#
#  示例 1：
#
#
# 输入：stones = [0,1,3,5,6,8,12,17]
# 输出：true
# 解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然
# 后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
#
#  示例 2：
#
#
# 输入：stones = [0,1,2,3,4,8,9,11]
# 输出：false
# 解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
#
#
#
#  提示：
#
#
#  2 <= stones.length <= 2000
#  0 <= stones[i] <= 2³¹ - 1
#  stones[0] == 0
#
#  Related Topics 数组 动态规划 👍 397 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return True

        @lru_cache(None)
        def dfs(idx, step):
            """
            dfs(pos,step)表示 如果青蛙经过步数为step的跳跃到达位置在pos的石头 它能否跳跃到终点
            因为是step跳跃到达的pos，所以再往下可以跳跃step, step+1, step-1, 但是需要注意只能向前跳, 即step+d>0, 并且必须跳到石头上(即pos+step+d in stones)
            """
            if idx == stones[-1]: return True
            steps = [step - 1, step, step + 1]
            for s in steps:
                if s and idx + s in stones:
                    if dfs(idx + s, s):
                        return True
            return False

        return dfs(0, 0)

    def dy_canCross(self, stones):
        """
        定义dp为字典，其中key=stone, value={可以到达stone的跳跃步长组成的集合}。那么能够到达stone等价于dp[stone]非空
        """
        dp = defaultdict(set)
        dp[0] = {0}
        for s in stones:
            for step in dp[s]:
                for d in [-1, 0, 1]:
                    if step + d and s + step + d in stones:
                        dp[s+step+d].add(step + d)
        return dp[stones[-1]] == set()
# leetcode submit region end(Prohibit modification and deletion)
