# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
#  例如，
#
#  [2,3,4] 的中位数是 3
#
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
#  设计一个支持以下两种操作的数据结构：
#
#
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。
#  double findMedian() - 返回目前所有元素的中位数。
#
#
#  示例：
#
#  addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
#  进阶:
#
#
#  如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
#  如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#  Related Topics 设计 双指针 数据流 排序 堆（优先队列） 👍 643 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class MedianFinder:

    def __init__(self):
        self.que_max = []
        self.que_min = []

    def addNum(self, num: int) -> None:
        que_min = self.que_min
        que_max = self.que_max
        if not que_min or num <= -que_min[0]:
            heapq.heappush(que_min, -num)
            if len(que_max) + 1 < len(que_min):
                heapq.heappush(que_max, -heapq.heappop(que_min))
        else:
            heapq.heappush(que_max, num)
            if len(que_max) > len(que_min):
                heapq.heappush(que_min, -heapq.heappop(que_max))

    def findMedian(self) -> float:
        que_min = self.que_min
        que_max = self.que_max
        if len(que_min) > len(que_max):
            return -que_min[0]
        return (-que_min[0] + que_max[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
