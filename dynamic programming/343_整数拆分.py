class Solution:
    def integerBreak1(self, n: int) -> int:
        if n < 3: return 1 * (n - 1)
        p = 1
        while n >= 5:
            p *= 3
            n -= 3
            print(n, p)
        res = p * n
        return res



if __name__ == '__main__':
    Solution().integerBreak1(10)
