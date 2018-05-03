# coding=utf-8
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None

        # 用一个二维数组表示每次运算最大值和最小值
        res = [[0, 0] for i in range(n)]

        res[0][0], res[0][1] = nums[0], nums[0]

        max_value = nums[0]

        index = 1
        while index < n:
            # 一个可能的最值（最大最小不知）
            t1 = res[index - 1][0] * nums[index]
            # 另一个可能的最值（最大最小不知）
            t2 = res[index - 1][1] * nums[index]

            # min
            res[index][1] = min(t1, t2, nums[index])

            # max
            res[index][0] = max(t1, t2, nums[index])

            max_value = max(res[index][0], max_value)

            index += 1
        return max_value