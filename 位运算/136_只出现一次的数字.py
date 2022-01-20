# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
#  说明：
#
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
#  示例 1:
#
#  输入: [2,2,1]
# 输出: 1
#
#
#  示例 2:
#
#  输入: [4,1,2,1,2]
# 输出: 4
#  Related Topics 位运算 数组 👍 2205 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        异或运算有以下三个性质。

        任何数和 0 做异或运算，结果仍然是原来的数，即 a ^ 0 = a。
        任何数和其自身做异或运算，结果是 0，即 a ^ a = 0。
        异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b
        """
        return reduce(lambda x, y: x ^ y, nums)
# leetcode submit region end(Prohibit modification and deletion)
