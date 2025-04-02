from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2
        # 转换为从nums中选择任意数字, 和是否为 target
        # dp[j]表示 背包总容量是i，最⼤可以凑成i的⼦集总和为dp[i]
        dp = [0] * (target + 1)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[-1] == target


if __name__ == '__main__':
    Solution().canPartition([1, 5, 11, 5])