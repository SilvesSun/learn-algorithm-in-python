# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
#  示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
#  提示：
#
#
#  n == height.length
#  1 <= n <= 2 * 10⁴
#  0 <= height[i] <= 10⁵
#
#
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 5022 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        # 每列能存多少水, 需要关注的是没个位置左右最大高度的较小值, 只有在左右较小值大于当前列的时候才能存下水
        # 两端不用考虑, 因为总有一边存不下水. 所以遍历位置为1~n-1
        # tle
        total = 0
        n = len(height)
        for i in range(1, n-1):
            max_left = 0
            for j in range(0, i):
                if height[j] > max_left:
                    max_left = height[j]

            max_right = 0
            for j in range(i+1, n):
                if height[j] > max_right:
                    max_right = height[j]

            # 较小值
            h = min(max_left, max_right)
            if h > height[i]:
                total += (h - height[i])
        return total

    def trap2(self, height: List[int]) -> int:
        # 上面的方法重复寻找了没个位置的左右最大值, 可以单次遍历
        # 执行耗时:40 ms,击败了98.64% 的Python3用户
        # 内存消耗:18.5 MB,击败了20.82% 的Python3用户
        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])

        total = 0
        for i in range(n):
            m = min(left[i], right[i])
            if m > height[i]:
                total += (m - height[i])
        return total

    def trap3(self, height):
        # 定义左右指针两边的最大值lMax和rMax分别表示height[0,l]和height[r,...]
        n = len(height)
        l_max = height[0]
        r_max = height[n-1]

        total = 0
        l = 0
        r = n - 1
        while l < r:
            # // 只需要知道较小的就行，一旦满足这个条件，不需要关注另一边的情况，因为从全局来看这部分一定会被“接”到
            if l_max < r_max:
                total += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
            else:
                total += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])
        return total

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().trap2([4,2,0,3,2,5]))