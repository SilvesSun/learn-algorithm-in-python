# 给定由
#  n 个小写字母字符串组成的数组
#  strs ，其中每个字符串长度相等。
#
#  选取一个删除索引序列，对于
#  strs 中的每个字符串，删除对应每个索引处的字符。
#
#  比如，有
#  strs = ["abcdef","uvwxyz"] ，删除索引序列
#  {0, 2, 3} ，删除后为
#  ["bef", "vyz"] 。
#
#  假设，我们选择了一组删除索引
#  answer ，那么在执行删除操作之后，最终得到的数组的行中的 每个元素 都是按字典序排列的（即 (strs[0][0] <= strs[0][1] <=
#  ... <= strs[0][strs[0].length - 1]) 和 (strs[1][0] <= strs[1][1] <= ... <= strs[
# 1][strs[1].length - 1]) ，依此类推）。
#
#  请返回
#  answer.length 的最小可能值 。
#
#
#
#  示例 1：
#
#
# 输入：strs = ["babca","bbazb"]
# 输出：3
# 解释：
# 删除 0、1 和 4 这三列后，最终得到的数组是 strs = ["bc", "az"]。
# 这两行是分别按字典序排列的（即，strs[0][0] <= strs[0][1] 且 strs[1][0] <= strs[1][1]）。
# 注意，strs[0] > strs[1] —— 数组 strs 不一定是按字典序排列的。
#
#
#  示例 2：
#
#
# 输入：strs = ["edcba"]
# 输出：4
# 解释：如果删除的列少于 4 列，则剩下的行都不会按字典序排列。
#
#
#  示例 3：
#
#
# 输入：strs = ["ghi","def","abc"]
# 输出：0
# 解释：所有行都已按字典序排列。
#
#
#
#
#  提示：
#
#
#
#  n == strs.length
#  1 <= n <= 100
#  1 <= strs[i].length <= 100
#  strs[i] 由小写英文字母组成
#
#
#  Related Topics 数组 字符串 动态规划 👍 86 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # 本质是求递增序列, 要使结果尽可能的小, 那么就要使递增序列尽可能长, 即 lis
        # 不一样的地方是限制条件从单个数组变成了多个字符串
        # 可以认为 354(俄罗斯套娃信封) -> 1691(堆叠长方体) -> 960 删列造序 是同一个思路
        if not strs: return 0
        n = len(strs)
        s0 = strs[0]
        ns = len(s0)
        dp = [1 for _ in range(ns)]
        for i in range(1, ns):
            for j in range(i):
                if s0[j] <= s0[i] and all([strs[k][j] <= strs[k][i] for k in range(1, n)]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return ns - max(dp)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    strs = ["babca", "bbazb"]
    print(Solution().minDeletionSize(strs))
