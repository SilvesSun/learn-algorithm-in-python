from typing import List


class Solution:
    def find_max_form(self, strs: List[str], m, n):
        # 在满足容量为m,n的背包中, 能获取到的最大价值为多少. 每个str的价值为1
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            countZero = s.count('0')
            countOne = s.count('1')
            for i in range(m, countZero - 1, -1):
                for j in range(n, countOne - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - countZero][j - countOne] + 1)
        return dp[m][n]


if __name__ == '__main__':
    print(Solution().find_max_form(["10", "0001", "111001", "1", "0"], 5, 3))
