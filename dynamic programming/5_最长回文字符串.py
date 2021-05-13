class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp
        # 如果一个字符串是回文串, 且长度大于2, 那么去掉它首尾的字母后, 依然为回文串
        # P(i,j) 表示字符串从i到j的字母组成的串是否为回文串
        # p(i,j) = p(i+1, j-1) && s(i) == s(j)
        # 即s[i+1: j-1]是回文串, 并且s的第i个和j个字母相同时, s[i:j]才是回文串
        n = len(s)
        if n < 2: return s
        max_len = 1
        start = 0
        # dp[i][j]表示s[i:j]是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for l in range(2, n + 1):
            for i in range(n):
                # l 表示字串长度, 则右边界假设为j, j-i + 1 = l
                j = l + i - 1
                if j >= n: break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                        # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
        return s[start:start + max_len]


if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))