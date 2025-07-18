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

        # g[l][r] 代表 [l,r] 这一段是否为回文串
        # 要想 g[l][r]=true ，必须满足以下两个条件
        # 1. s[l] == s[r]
        # 2. g[l+1][r-1] = true


        g = [[False] * n for _ in range(n)]
        for r in range(n):
            for l in range(r, -1, -1):
                if l == r:
                    g[l][r] = True
                else:
                    if s[l] == s[r] and (r -l  == 1 or g[l + 1][r - 1]):
                        g[l][r] = True

        from pprint import pprint
        pprint(g)

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
if __name__ == '__main__':
    s = "leet"
    print(Solution().minCut(s))