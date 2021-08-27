# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
#
#  每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
#
#  返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
#
#
#
#  示例 1：
#
#  输入：people = [1,2], limit = 3
# 输出：1
# 解释：1 艘船载 (1, 2)
#
#
#  示例 2：
#
#  输入：people = [3,2,2,1], limit = 3
# 输出：3
# 解释：3 艘船分别载 (1, 2), (2) 和 (3)
#
#
#  示例 3：
#
#  输入：people = [3,5,3,4], limit = 5
# 输出：4
# 解释：4 艘船分别载 (3), (3), (4), (5)
#
#  提示：
#
#
#  1 <= people.length <= 50000
#  1 <= people[i] <= limit <= 30000
#
#  Related Topics 贪心 数组 双指针 排序
#  👍 130 👎 0


from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        light = 0
        heavy = n - 1
        res = 0
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            res += 1
        return res

if __name__ == '__main__':
    people = [3, 2, 2, 1]
    limit = 3
    print(Solution().numRescueBoats(people, limit))
