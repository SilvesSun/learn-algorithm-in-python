from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end_pos, step = 0, 0, 0
        for i in range(n - 1):
            # 从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1
            if max_pos >= i:  # 当前能到达的最远的距离
                max_pos = max(max_pos, i + nums[i])
                if i == end_pos: # 已到达边界
                    end_pos = max_pos
                    step += 1
        return step
