from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n < 3: return 0
        total = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                total += k - j

        return total

if __name__ == '__main__':
    nums = [4, 2, 3, 4]
    print(Solution().triangleNumber(nums))
