# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,0]
# 输出：3
#
#
#  示例 2：
#
#
# 输入：nums = [3,4,-1,1]
# 输出：2
#
#
#  示例 3：
#
#
# 输入：nums = [7,8,9,11,12]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5 * 105
#  -231 <= nums[i] <= 231 - 1
#
#  Related Topics 数组 哈希表
#  👍 1304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        如果数组中包含 x ,x∈[1,N]，那么恢复后，数组的第 x - 1 个元素为 x

        在恢复后，数组应当有 [1, 2, ..., N] 的形式，但其中有若干个位置上的数是错误的，每一个错误的位置就代表了一个缺失的正数。以题目中的示例二 [3, 4, -1, 1]
        为例，恢复后的数组应当为 [1, -1, 3, 4]，我们就可以知道缺失的数为 2

        那么我们如何将数组进行恢复呢？我们可以对数组进行一次遍历，对于遍历到的数 x, x=nums[i]，如果 x∈[1,N]，我们就知道 x 应当出现在数组中的 x−1 的位置，
        因此交换 nums[i] 和 nums[x−1]，这样 x 就出现在了正确的位置。在完成交换后，新的 nums[i] 可能还在 [1,N] 的范围内，我们需要继续进行交换操作，
        直到 x notin [1, N]

        注意到上面的方法可能会陷入死循环。如果 nums[i] 恰好与 nums[x−1] 相等，那么就会无限交换下去。此时我们有 nums[i]==x== nums[x-1]，
        说明 x 已经出现在了正确的位置。因此我们可以跳出循环，开始遍历下一个数

        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().firstMissingPositive([3,4,-1,1]))