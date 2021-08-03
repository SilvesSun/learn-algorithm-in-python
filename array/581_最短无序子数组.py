from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        n = len(nums)
        start = 0
        end = len(nums) - 1
        while start < n:
            if nums[start] == sort_nums[start]:
                start += 1
            else:
                break
        while end >= 0:
            if nums[end] == sort_nums[end]:
                end -= 1
            else:
                break
        return end - start + 1 if end > start else 0


if __name__ == '__main__':
    nums = [1]
    print(Solution().findUnsortedSubarray(nums))
