class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current = nums[0]
        m = current
        for i in range(1, len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(current, m)
        return m

    def dynamic_max_sub_array(self, nums):
        n = len(nums)
        dp = [-float('INF')] * n
        dp[0] = nums[0]
        m = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            m = max(dp[i], m)
        return m

    def maxSubArray2(self, nums):
        """
        分冶法
        :param nums:
        :return:
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left == right: return nums[left]
        mid = (left + right) / 2

        left_max = sum_num = 0
        for i in range(mid - 1, left - 1, -1):
            sum_num += nums[i]
            left_max = max(left_max, sum_num)

        right_max = sum_num = 0
        for i in range(mid + 1, right + 1):
            sum_num += nums[i]
            right_max = max(right_max, sum_num)

        left_ans = self.helper(nums, left, mid - 1)
        right_ans = self.helper(nums, mid + 1, right)

        return max(left_max + nums[mid] + right_max, max(left_ans, right_ans))


nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print(s.dynamic_max_sub_array(nums))
