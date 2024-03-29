# 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 素数 组成，且其中所有整数互不相同。
#
#  对于每对满足 0 < i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
#
#  那么第 k 个最小的分数是多少呢? 以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == a
# rr[j] 。
#
#
#  示例 1：
#
#
# 输入：arr = [1,2,3,5], k = 3
# 输出：[2,5]
# 解释：已构造好的分数,排序后如下所示:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3
# 很明显第三个最小的分数是 2/5
#
#
#  示例 2：
#
#
# 输入：arr = [1,7], k = 1
# 输出：[1,7]
#
#
#
#
#  提示：
#
#
#  2 <= arr.length <= 1000
#  1 <= arr[i] <= 3 * 104
#  arr[0] == 1
#  arr[i] 是一个 素数 ，i > 0
#  arr 中的所有数字 互不相同 ，且按 严格递增 排序
#  1 <= k <= arr.length * (arr.length - 1) / 2
#
#  Related Topics 数组 二分查找 堆（优先队列）
#  👍 123 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Item:
    def __init__(self, x, y, idx, idy):
        self.x = x
        self.y = y
        self.idx = idx
        self.idy = idy

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x

    def __repr__(self):
        return f'[{self.x}, {self.y}, {self.idx}, {self.idy}]'


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Item(arr[0], arr[i], 0, i) for i in range(1, n)]
        heapq.heapify(q)
        for _ in range(k-1):
            item = heapq.heappop(q)
            i, j = item.idx, item.idy
            if i + 1 < j:
                heapq.heappush(q, Item(arr[i+1], arr[j], i+1, j))
        return [q[0].x, q[0].y]


if __name__ == '__main__':
    print(Solution().kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
