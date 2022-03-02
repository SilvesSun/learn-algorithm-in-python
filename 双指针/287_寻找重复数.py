# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
#
#  假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
#
#  你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,3,4,2,2]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：nums = [3,1,3,4,2]
# 输出：3
#
#
#
#
#  提示：
#
#
#  1 <= n <= 10⁵
#  nums.length == n + 1
#  1 <= nums[i] <= n
#  nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
#
#
#
#
#  进阶：
#
#
#  如何证明 nums 中至少存在一个重复的数字?
#  你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
#
#  Related Topics 位运算 数组 双指针 二分查找 👍 1599 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        分析这个数组，索引从 0～n0～n ，值域是 1～n1～n 。值域，在索引的范围内，值可以当索引使。
        比如，nums 数组：[4, 3, 1, 2, 2][4,3,1,2,2]
        以 nums[0] 的值 4 作为索引，去到 nums[4]
        以 nums[4] 的值 2 作为索引，去到 nums[2]
        以 nums[2] 的值 1 作为索引，去到 nums[1]……
        从一项指向另一项，将nums数组抽象为链表：4->2->1->3->2，如下图，链表有环。

        """
        slow, fast = 0, 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        find =0
        while 1:
            find = nums[find]
            slow = nums[slow]
            if slow == find:
                break
        return slow
# leetcode submit region end(Prohibit modification and deletion)
