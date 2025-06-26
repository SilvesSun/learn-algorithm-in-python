# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
#
#  每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j
# < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
#
#  如果无法让 arr1 严格递增，请返回 -1。
#
#
#
#  示例 1：
#
#
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# 输出：1
# 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
#
#
#  示例 2：
#
#
# 输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# 输出：2
# 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
#
#
#  示例 3：
#
#
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# 输出：-1
# 解释：无法使 arr1 严格递增。
#
#
#
#  提示：
#
#
#  1 <= arr1.length, arr2.length <= 2000
#  0 <= arr1[i], arr2[i] <= 10^9
#
#
#
#
#  Related Topics 数组 二分查找 动态规划 排序 👍 238 👎 0
import bisect
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # 定义 f(i) 为使数组 arr1 的前 i+1 项（下标 0∼i）递增，且 保留 arr1[i] 的情况下的最小替换次数
        # 为什么要不替换 arr1[i] 呢？因为如果替换，那么到底替换成哪个数，就得另加一个状态维护。可如果 arr1 的最后一项也要替换呢？我们可以在数组最后增加一个非常大的数，而这个数不替换即可
        # 首先将 arr2 从小到大排序，去重。
        # 考虑 f(i)，由于我们不能替换 arr1[i]，那么我们考虑是否替换 arr1[i-1]（如果有）

        # 1. 如果替换 arr1[i-1]
        # arr1[i-1] 应当越大越好，但是不能等于或超过 arr1[i]。我们可以二分查找出 arr2 中第一个等于或超过 arr1[i] 的数 arr2[j]，然后将 arr1[i-1] 替换为 arr2[j-1]
        # 我们可以继续考虑 arr1[i-2] （如果有），如果仍然想替换它，那么显然 arr2[j-1] 是不能再用了，应当选择更小一点的 arr2[j-2] （如果有）。以此类推，我们还可以继续把 arr1[i-3] 替换成 arr2[j-3]，等等等等，直到我们不想再替换。

        # 设已经替换了 k 个数而我们不想再替换了，那就意味着需要保留 arr1[i-k-1]，但这是有条件的，由于 arr1[i-k] 被替换成了 arr2[j-k]，故只有当 arr1[i-k-1]<arr2[j-k] 才可以保证序列递增。
        # 若我们保留 arr1[i-k-1]，问题就可以被转化为 f(i−k−1)+k。

        # 我们可以枚举 k 进行状态转移。显然 k 不能超过 j，也就是最多可供替换的 arr2 的数字个数；另外 k 也不能超过 i，也就是最多能被替换的 arr1 的数字个数。
        # 但是有个问题，如果 k=i，那么 arr1[i-k-1]=arr1[-1] 是不存在的。解决方案是在 arr1 之前添加一个非常小的数（如 −1），然后令 k 不超过 i−1 即可。此时的 arr1[0] 充当了前面的 arr1[-1] 的作用。

        # 2. 如果不替换 arr1[i-1], 则需要满足 arr1[i-1] < arr1[i]，此时 f(i)=min(f(i),f(i−1))
        # 我们在 arr1 的两侧加上哨兵： arr1 = [-1] + arr1 + [inf]

        # 状态转移方程
        # f(0) = 0
        # f(i) = min(f(i-k-1) + k), i >= 1, 1 <=k <= min(i-1, j), arr1[i-k-1] < arr2[j-k]
        # f(i) = min(f(i-1)), i >= 1, arr1[i-1] < arr1[i]

        arr1 = [-1] + arr1 + [float('inf')]
        arr2 =  sorted(set(arr2))

        n = len(arr1)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            j = bisect.bisect_left(arr2, arr1[i])
            for k in range(1, min(i-1, j) + 1):
                if arr1[i-k-1] < arr2[j-k]:
                    dp[i] = min(dp[i], dp[i-k-1] + k)
            if arr1[i-1] < arr1[i]:
                dp[i] = min(dp[i], dp[i-1])
        return dp[-1] if dp[-1] != float('inf') else -1

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 3, 2, 4]
    Solution().makeArrayIncreasing(arr1, arr2)