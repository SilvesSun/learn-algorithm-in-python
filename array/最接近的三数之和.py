# coding=utf-8
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        先设定三个指针left, mid, right。初始时，left为数组最左端的元素，且固定不变，mid = left + 1, right为数组最右端的元素。
        然后对 left, mid, right三个指针所指向的值求和，记为sum_val

        设置一个值min_gap记录当前的最小差，令abs(sum_val - target)的值与min_gap比较，若比min_gap小，则说明获得了更接近的三数之和，
        更新min_gap；若比min_gap大，则有两种可能性：

        1. sum_val - target > 0，说明现在的三数之和大了，则令right指针左移

        2. sum_val - target < 0，说明现在的三数之和小了，则令mid指针右移

        此循环终止的条件是mid >= right
        """

        nums.sort()
        length = len(nums)
        res = sum(nums[:3])

        min_gap = abs(target - res)
        for l in range(length):
            m = l + 1
            r = length - 1
            while m < r:
                c_sum = nums[l] + nums[m] + nums[r]
                tem = abs(target - c_sum)
                if tem < min_gap:
                    min_gap = tem
                    res = c_sum
                else:
                    if c_sum - target > 0:
                        r -= 1
                    else:
                        m += 1
        return res

    def threeSumClosest2(self, nums, target):
        nums.sort()
        length = len(nums)
        sum_set = []

        for i, num in enumerate(nums):
            l = i + 1
            r = length - 1

            while l < r:
                c_sum = num + nums[l] + nums[r]
                sum_set.append(c_sum)

                if c_sum < target:
                    l += 1
                elif c_sum > target:
                    r -= 1
                else:
                    return target
        sum_set.sort(key=lambda x: abs(x-target))
        return sum_set[0]

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
s.threeSumClosest2(nums, target)
