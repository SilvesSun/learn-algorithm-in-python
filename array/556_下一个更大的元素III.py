# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
#
#  注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：n = 12
# 输出：21
#
#
#  示例 2：
#
#
# 输入：n = 21
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= n <= 2³¹ - 1
#
#  Related Topics 数学 双指针 字符串 👍 183 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        从后往前遍历，找到第一次出现后一个比前一个大的index, 然后再找到nums[index:]中的比nums[index - 1]大的最小数，然后交换，
        对交换后的nums[index:]从小到大排序
        """
        nums = list(str(n))
        nl = len(nums)
        idx = -1
        for i in range(nl - 1, -1, -1):
            # 查找到最后没有找到后一个比前一个大的index
            if i == 0:
                return -1
            if nums[i] > nums[i - 1]:
                idx = i - 1
                break
        # 在 idx 以后的都是降序的, 从后到 idx 查找第一个比 idx 大的数
        for i in range(nl - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[idx], nums[i] = nums[i], nums[idx]
                nums = nums[:idx + 1] + sorted(nums[idx + 1:])
                break

        res = int(''.join(nums))

        return res if res < 2 ** 31 else -1


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().nextGreaterElement(12))
