from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 在两堆石头中, 越接近 总质量 / 2, 最终的石头重量越下. 所以问题转换为如何选取石头的子集, 使得其重量和趋近总质量/2
        total = sum(stones)
        target = int(total / 2)
        # 考虑背包的容量, 1 <= stones.length <= 30 , 1 <= stones[i] <= 100 , 故总容量最大为 100*30/2
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return total - dp[target] - dp[target]


if __name__ == '__main__':
    print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]))
