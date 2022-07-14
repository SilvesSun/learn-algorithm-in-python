# 给定一个整数数组 asteroids，表示在同一行的行星。
#
#  对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
#
#  找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞
# 。
#
#
#
#  示例 1：
#
#
# 输入：asteroids = [5,10,-5]
# 输出：[5,10]
# 解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
#
#  示例 2：
#
#
# 输入：asteroids = [8,-8]
# 输出：[]
# 解释：8 和 -8 碰撞后，两者都发生爆炸。
#
#  示例 3：
#
#
# 输入：asteroids = [10,2,-5]
# 输出：[10]
# 解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
#
#
#
#  提示：
#
#
#  2 <= asteroids.length <= 10⁴
#  -1000 <= asteroids[i] <= 1000
#  asteroids[i] != 0
#
#  Related Topics 栈 数组 👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = deque()
        n = len(asteroids)
        s.append(asteroids[0])
        idx = 1
        while idx < n:
            num = asteroids[idx]
            if not s:
                s.append(num)
                idx += 1
                continue
            if num > 0:
                s.append(num)
            if num < 0:
                # 此时从栈中逐个弹出数据, 和当前元素对比
                if s[-1] < 0:
                    s.append(num)
                else:
                    while s:
                        last = s.pop()
                        # 相对方向才有可能碰撞
                        if last > 0:
                            if abs(num) > last:
                                # 此时最后一个元素破碎, 继续和剩余的栈内元素碰撞
                                if not s:
                                    s.append(num)
                                    break
                                if s[-1] < 0:
                                    s.append(num)
                                    break
                                continue
                            elif abs(num) == last:
                                # 两个元素抵消, 跳出
                                break
                            else:
                                s.append(last)
                                break
            idx += 1
        return list(s)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().asteroidCollision(asteroids=[1, -1, -2, -2]))
