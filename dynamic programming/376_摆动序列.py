class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0

        # 可能存在重复的值, 先去除重复值
        array = [nums[0]]
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                array.append(nums[i])

        # 现在array全部是不同的数字, 摆动的前提是相邻3个数直接差值为正负或者负正
        n = len(array)
        if n <= 2: return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for j in range(2, n):
            if (array[j] - array[j - 1]) * (array[j - 1] - array[j - 2]) < 0:
                dp[j] = 1 + dp[j - 1]
            else:
                dp[j] = dp[j - 1]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().wiggleMaxLength([3, 3, 3, 2, 5]))
