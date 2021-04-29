class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        将数组中前k项的最大连续子数组和记为f(k)。假设我们已经处理了k-1个，正在处理第k个。那么f(k)跟f(k-1)有什么关系？它必然是下列三种情况中最大的那个：

        - 前k-1项的最大子数组和
        - 当前数组第k项
        - 当前第k项，加上前面连续的若干项
        """

        max_len = len(nums)
        max_sum, max_tem = nums[0], nums[0]
        for i in range(max_len):
            if max_tem < 0:
                max_tem = nums[i]
            else:
                max_tem += nums[i]

            max_sum = max(max_sum, max_tem)
        return max_sum

    def max_sub_array(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        cmax = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            if cmax < dp[i]:
                cmax = dp[i]
        return cmax


s = Solution()
s.maxSubArray(
    [84, 38, 65, 52, -9, 70, 81, 58, -33, 87, -47, 48, 23, -53, 86, -2, 45, 56, 35, 5, 90, 47, -84, -21, 55, -8, 37, 0,
     -3, -60, -11, -42, 54, -68, -89, -54, -98, 68, 80, -31, 55, -67, 93, -45, -21, 79, 52, -75, 12, -12, 29, -21, -88,
     21, 57, 67, -87, -6, -33, -14, 10, 32, 44, -35, 63, 54, -13, 65, 22, -33, -66, -46, 0, -73, 8, 78, 82, -62, 79, -6,
     2])
