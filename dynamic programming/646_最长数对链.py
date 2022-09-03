# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
#
#  现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
#
#  给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
#
#
#
#  示例：
#
#
# 输入：[[1,2], [2,3], [3,4]]
# 输出：2
# 解释：最长的数对链是 [1,2] -> [3,4]
#
#
#
#
#  提示：
#
#
#  给出数对的个数在 [1, 1000] 范围内。
#
#  Related Topics 贪心 数组 动态规划 排序 👍 294 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 先排序
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 if pairs[i][0] > pairs[j][1] else 0)

        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]))
