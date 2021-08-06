from pprint import pprint
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] 表示以下标i-1结尾的nums1, 和以下标j-1结尾的nums2的最长重复子数组长度
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > res: res = dp[i][j]
        return res


if __name__ == '__main__':
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 1, 4]
    print(Solution().findLength(a, b))
