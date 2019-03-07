# coding=utf-8
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        这里的规则是劫匪不能同时抢劫相邻的屋子，即我们在累加时，只有两种选择：

        如果选择了抢劫上一个屋子，那么就不能抢劫当前的屋子，所以最大收益就是抢劫上一个屋子的收益

        如果选择抢劫当前屋子，就不能抢劫上一个屋子，所以最大收益是到上一个屋子的上一个屋子为止的最大收益，加上当前屋子里有的钱
        """
        length = len(nums)

        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])

        last_max = nums[0]  # 上次最大收益

        cur_max = max(nums[0], nums[1])
        for i in range(2, length):
            last_max, cur_max = cur_max, max(last_max+nums[i], cur_max)

        return cur_max

    def rob2(self, nums):
        n = len(nums)
        if not nums: return 0
        dp = [0 for _ in range(n)]

        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        for i in range(n):
            if i == 0: dp[0] = nums[0]
            if i == 1: dp[1] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]

nums = [1,2,3,1]
s = Solution()
print(s.rob2(nums))

