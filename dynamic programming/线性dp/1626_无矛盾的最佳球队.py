# 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。
#
#  然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间
# 不会发生矛盾。
#
#  给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队
# 中得分最高那支的分数 。
#
#
#
#  示例 1：
#
#  输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# 输出：34
# 解释：你可以选中所有球员。
#
#  示例 2：
#
#  输入：scores = [4,5,6,5], ages = [2,1,2,1]
# 输出：16
# 解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
#
#
#  示例 3：
#
#  输入：scores = [1,2,3,5], ages = [8,9,10,1]
# 输出：6
# 解释：最佳的选择是前 3 名球员。
#
#
#
#
#  提示：
#
#
#  1 <= scores.length, ages.length <= 1000
#  scores.length == ages.length
#  1 <= scores[i] <= 10⁶
#  1 <= ages[i] <= 1000
#
#
#  Related Topics 数组 动态规划 排序 👍 232 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = [(scores[i], ages[i]) for i in range(len(scores))]
        # 按照年龄排序
        arr.sort(key=lambda x: (x[1], x[0]))
        # 此时求最长递增子序列的序列本身
        lis = [i[0] for i in arr]
        dp = [0 for i in range(len(lis))]
        n = len(arr)
        for i in range(n):
            dp[i] = lis[i]
            for j in range(i):
                if lis[i] >= lis[j]:
                    dp[i] = max(dp[i], dp[j] + lis[i])
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    scores = [319776, 611683, 835240, 602298, 430007, 574, 142444, 858606, 734364, 896074]
    ages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(Solution().bestTeamScore(scores, ages))
