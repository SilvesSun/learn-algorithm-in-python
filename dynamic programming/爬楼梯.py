class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n)]
        dp[0] = 1
        if n >= 2:
            dp[1] = 2
            for i in range(2, n):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

    def climbStairs2(self, n):
        dp = [1, 2]
        if n <= 1:
            return dp[0]
        elif n == 2: return dp[1]
        else:
            for i in range(2, n):
                dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[1]


s = Solution()
print(s.climbStairs(6))
set()