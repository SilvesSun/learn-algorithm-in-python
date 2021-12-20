# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
#  在加热器的加热半径范围内的每个房屋都可以获得供暖。
#
#  现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
#
#  说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#
#
#  示例 1:
#
#
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#
#
#  示例 2:
#
#
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#
#
#  示例 3：
#
#
# 输入：houses = [1,5], heaters = [2]
# 输出：3
#
#
#
#
#  提示：
#
#
#  1 <= houses.length, heaters.length <= 3 * 104
#  1 <= houses[i], heaters[i] <= 109
#
#  Related Topics 数组 双指针 二分查找 排序
#  👍 267 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        # 对于每个房屋，要么用前面的暖气，要么用后面的，二者取近的，得到距离
        for i in range(len(houses)):
            cur = houses[i]
            if cur <= heaters[0]:
                d = heaters[0] - cur
            elif cur >= heaters[len(heaters) - 1]:
                d = cur - heaters[len(heaters) - 1]
            else:
                l = 0
                r = len(heaters) - 1
                while l < r:
                    mid = (l + r) >> 1
                    if heaters[mid] < houses[i]:
                        l = mid + 1
                    else:
                        r = mid
                d = min(heaters[l] - houses[i], houses[i] - heaters[l - 1])
            ans = max(ans, d)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().findRadius(houses=[1, 2, 3], heaters=[1, 2, 3]))
