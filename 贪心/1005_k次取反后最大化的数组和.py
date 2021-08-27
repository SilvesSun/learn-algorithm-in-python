from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        less_z = []
        i = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                less_z.append(nums[i])
            else:
                break
        # 当前负数集合的长度
        n = len(less_z)
        if k <= n:
            # 尽可能的将负数转为整数
            return -sum(nums[:k]) + sum(nums[i:]) + sum(nums[k: i])
        else:
            # 全部转为正数后还需要翻转, 需要翻转次数为 k - n
            positive_n = sorted([abs(i) for i in nums])
            k = k - n
            # 此时每次只翻转最小的值, 若k为偶数, 则最终全为正数, 否则第一个为负数
            if k % 2 == 0:
                return sum(positive_n)
            else:
                return sum(positive_n[1:]) - positive_n[0]


if __name__ == '__main__':
    print(Solution().largestSumAfterKNegations([4, 2, 3], 1))