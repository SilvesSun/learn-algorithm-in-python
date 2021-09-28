# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
#
#  已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
#
#  每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎
# ，则可以在之后的操作中 重复使用 这枚鸡蛋。
#
#  请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
#
#  示例 1：
#
#
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
# 如果它没碎，那么肯定能得出 f = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
#
#
#  示例 2：
#
#
# 输入：k = 2, n = 6
# 输出：3
#
#
#  示例 3：
#
#
# 输入：k = 3, n = 14
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= k <= 100
#  1 <= n <= 104
#
#  Related Topics 数学 二分查找 动态规划
#  👍 686 👎 0


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 状态分为鸡蛋个数和楼层数
        # 状态可以表示成 (k, n)，其中 k 为鸡蛋数，n 为楼层数。当我们从第 x 楼扔鸡蛋的时候：
        #
        # 如果鸡蛋不碎，那么状态变成 (k, n-x)，即我们鸡蛋的数目不变，但答案只可能在上方的 n-x 层楼了。也就是说，我们把原问题缩小成了一个规模为 (k, n-x) 的子问题；
        #
        # 如果鸡蛋碎了，那么状态变成 (k-1, x-1)，即我们少了一个鸡蛋，但我们知道答案只可能在第 x 楼下方的 x-1 层楼中了。也就是说，我们把原问题缩小成了一个规模为 (k-1, x-1) 的子问题。
        # dp[k][n] = 1 + min(max(dp[k-1][x-1], dp[k][n-x])

        memo = {}

        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('INF')
            # for i in range(1, n + 1):
            #     res = min(res, max(dp(k - 1, i - 1), dp(k, n - i))+ 1)
            lo, hi = 1, n
            while lo <= hi:
                mid = (lo + hi) >> 1
                broken = dp(k - 1, mid - 1)
                not_broken = dp(k, n - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)

            memo[(k, n)] = res
            return res

        return dp(k, n)


print(Solution().superEggDrop(2, 100))
