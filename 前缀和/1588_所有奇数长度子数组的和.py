from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        pre_sum = [0] * n
        for i in range(n):
            if i - 1 >= 0:
                pre_sum[i] = arr[i] + pre_sum[i-1]
            else:
                pre_sum[i] = arr[i]

        for i in range(n):
            for j in range(i, n, 2):
                if i + j - 1 < n: # not out boundary
                    if i - 1 < 0:
                        ans += pre_sum[i]
                    else:
                        ans += pre_sum[i+j-1] - pre_sum[i-1]
        return ans

if __name__ == '__main__':
    Solution().sumOddLengthSubarrays([1,4,2,5,3])