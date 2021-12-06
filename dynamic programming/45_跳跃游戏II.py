from typing import List

"""
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。

"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end_pos, step = 0, 0, 0
        for i in range(n - 1):
            # 从左到右遍历数组，到达边界时，更新边界并将跳跃次数增加 1
            if max_pos >= i:  # 当前能到达的最远的距离
                max_pos = max(max_pos, i + nums[i])
                if i == end_pos:  # 已到达边界
                    end_pos = max_pos
                    step += 1
        return step


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))
