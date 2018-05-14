# coding=utf-8
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 每个正整数均可表示为4个整数的平方和 四平方和定理
        # 两个定理:
        # 如果一个数能被4整除, 那么我们可以把4都去掉, 并不影响结果，比如2和8,3和12等等，返回的结果都相同
        # 如果一个数除以8余7的话，那么肯定是由4个完全平方数组成
        # 首先生成小于该数的所有的平方数
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7: return 4

        # 这两步做完, 可能的结果是1, 2, 3
        # 首先考虑1, 这个时候的平方数正好为n; 然后2, 这种时候为两个平方数之和.
        i = 0
        while i*i <= n:
            j = int(pow(n - i*i, 0.5))
            print(i, j)
            if i ** 2 + j ** 2 == n:
                if i == 0 or j == 0:
                    return 1
                else:
                    return 2
            i += 1

        return 3

    def numSquares2(self, n):
        dp = [sys.maxint for _ in range(n+1)]
        i = 0
        while i ** 2 <= n:
            dp[i ** 2] = 1
            i += 1

        i = 1
        while i <= n:
            j = 1
            while i + j ** 2 <= n:
                dp[i+j**2] = min(dp[i]+1, dp[i+j**2])
                j += 1
            i += 1
        return dp[n]


s = Solution()
print(s.numSquares2(5))