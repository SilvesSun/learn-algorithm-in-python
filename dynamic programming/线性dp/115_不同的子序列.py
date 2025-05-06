# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。
#
#  测试用例保证结果在 32 位有符号整数范围内。
#
#
#
#  示例 1：
#
#
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit
#
#  示例 2：
#
#
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下所示, 有 5 种可以从 s 中得到 "bag" 的方案。
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#
#
#
#
#  提示：
#
#
#  1 <= s.length, t.length <= 1000
#  s 和 t 由英文字母组成
#
#
#  Related Topics 字符串 动态规划 👍 1342 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] 表示 s 的前 i 个字符中 t 的前 j 个字符出现的次数
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 空字符串t是任何字符串的子序列
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, min(i, n) + 1):
                if s[i - 1] == t[j - 1]:
                    # 匹配当前字符 + 不匹配当前字符
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

# leetcode submit region end(Prohibit modification and deletion)
