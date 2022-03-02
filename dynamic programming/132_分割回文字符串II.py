# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
#
#  返回符合要求的 最少分割次数 。
#
#
#
#
#
#  示例 1：
#
#
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#
#
#  示例 2：
#
#
# 输入：s = "a"
# 输出：0
#
#
#  示例 3：
#
#
# 输入：s = "ab"
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 2000
#  s 仅由小写英文字母组成
#
#
#
#  Related Topics 字符串 动态规划 👍 543 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        # dp[i] 定义为字符串[0,i]的回文子串, 最少分割次数为 dp[i]
        # 要求[0, i] 的子串进行分割, 假设分割点为j, 使得分割后[j+1, i] 为回文字符串, 说明 dp[i] = dp[j] + 1, 同时由于要求最小次数,
        # dp[i] = min(dp[i], dp[j] + 1), 遍历过程中取最小值
        n = len(s)
        g = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        dp = [float('inf')] * n

        for i in range(n):
            if g[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
