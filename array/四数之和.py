# coding=utf-8
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 将其转换为三数之和, 首先确定首尾两指针, 然后中间两指针按照三数之和操作

        nums.sort()
        length = len(nums)
        res = []
        if length < 4: return []
        for i in range(length):
            if i !=0 and nums[i] == nums[i-1]: continue # 跳过相同的数
            for j in range(i+1, length):
                if j != i+1 and nums[j] == nums[j-1]: continue
                m = j + 1
                n = length - 1

                while m < n:
                    c_sum = nums[i] + nums[j] + nums[m] + nums[n]
                    if m != j+1 and nums[m] == nums[m-1]: m += 1
                    elif n != length-1 and nums[n] == nums[n+1]: n -= 1

                    elif c_sum > target: n -= 1
                    elif c_sum < target: m += 1
                    elif c_sum == target:
                        c_res = [nums[i], nums[j], nums[m], nums[n]]
                        m += 1
                        n -= 1
                        if c_res not in res: res.append(c_res)
        print(res)
        return res

s = Solution()
nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9

s.fourSum(nums, target)

