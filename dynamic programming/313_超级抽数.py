from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        m = len(primes)
        p = [1 for _ in range(len(primes))]

        for i in range(2, n + 1):
            min_num = min(dp[p[j]] * primes[j] for j in range(m))
            dp[i] = min_num
            for j in range(m):
                if dp[p[j]] * primes[j] == min_num:
                    p[j] += 1

        return dp[-1]


if __name__ == '__main__':
    n = 12
    primes = [2, 7, 13, 19]
    print(Solution().nthSuperUglyNumber(n, primes))
