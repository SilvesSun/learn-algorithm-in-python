class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        # dp[i]表示在输入数组nums升序的情况下, 以nums[i]为最大整数的 整除子集的 大小, 这种情况下nums[i]一定被
        # 选取
        n = len(nums)
        dp = [1] * n
        max_size = 1
        max_val = -1
        for i in range(n):
            t = nums[i]
            for j in range(i):
                if t % nums[j] == 0:
                    dp[i] = max(dp[i], 1 + dp[j])
            if dp[i] > max_size:
                max_size = dp[i]
                max_val = nums[i]

        ans = []
        idx = n - 1
        for size in range(max_size, 0, -1):
            while dp[idx] != size or max_val % nums[idx] != 0:
                idx -= 1
            max_val = nums[idx]
            ans.append(max_val)
        return ans


if __name__ == '__main__':
    print(Solution().largestDivisibleSubset([2, 4, 7, 8, 9, 12, 16, 18]))
