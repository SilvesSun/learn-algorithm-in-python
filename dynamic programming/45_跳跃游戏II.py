from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        m = max(nums)
        n = len(nums)
        dp = [m] * n
        dp[0] = 0
        dp[1] = 1


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))
