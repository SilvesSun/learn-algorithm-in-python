class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        p1 = 1
        p2 = 1
        p3 = 1
        for i in range(2, n + 1):
            t1, t2, t3 = 2 * p1, 3 * p2, 5 * p3
            dp[i] = min(t1, t2, t3)
            if dp[i] == t1:
                p1 += 1
            if dp[i] == t2:
                p2 += 1
            if dp[i] == t3:
                p3 += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))
