# 给你一个整数数组 nums 和一个整数 target 。
#
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
#
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
#
#
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        添加+ - 号, 相当于一部分 和-差=target, 即 sum_plus - sum_dif = target
        记数组的元素和为 sum, 则 sum_dif = sum - sum_plus, sum_plus - (sum-sum_plus) = target, sum_plus = (sum + target) / 2
        其中 sum + target需要为非负偶数.

        问题转化为在数组中选择若干元素, 使得和为sum_dif. 转换为01背包问题, 即装满容量为sum_dif的背包, 有几种办法

        dp[j]表示装满j这么大容积的包, 有dp[j]种办法

        不考虑nums[i]的情况下，填满容量为j - nums[i]的背包，有dp[j - nums[i]]中方法。那么只要搞到nums[i]的话，凑成dp[j]就有dp[j - nums[i]] 种方法

        dp[j] += dp[j-nums[i]]
        """

        # 对于01背包问题一维dp的遍历，nums放在外循环，target在内循环，且内循环倒序
        sum_val = sum(nums)
        # 所有数字相加比目标值小, 无方案
        if target > sum_val: return 0

        if (sum_val + target) % 2 == 1: return 0

        # 背包容量
        bag_volume = (sum_val + target) // 2
        # 初始化
        dp = [0] * (bag_volume + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bag_volume, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[bag_volume]


if __name__ == '__main__':
    nums = [1000]
    target = 1000

    print(Solution().findTargetSumWays(nums, target))
