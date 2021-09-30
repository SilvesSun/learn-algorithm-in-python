# 给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。
#
#  每个矩形由其 左下 顶点和 右上 顶点坐标表示：
#
#
#
#  第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
#  第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。
#
#
#
#
#
#  示例 1：
#
#
# 输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# 输出：45
#
#
#  示例 2：
#
#
# 输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# 输出：16
#
#
#
#
#  提示：
#
#
#  -104 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 104
#
#  Related Topics 几何 数学
#  👍 133 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1 = (ax2 - ax1) * (ay2 - ay1)
        rect2 = (bx2 - bx1) * (by2 - by1)
        if ax2 < bx1 or ax1 > bx2 or ay1 > by2 or ay2 < by1:
            return rect1 + rect2
        else:
            x_list = sorted([ax1, ax2, bx1, bx2])
            y_list = sorted([ay1, ay2, by1, by2])
            # 重叠部分
            overlay = (x_list[2] - x_list[1]) * (y_list[2]-y_list[1])
            return rect1 - overlay + rect2

print(Solution().computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2))
