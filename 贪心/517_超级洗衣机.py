# 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
#
#  在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
#
#  给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。如果不能使每台洗衣
# 机中衣物的数量相等，则返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：machines = [1,0,5]
# 输出：3
# 解释：
# 第一步:    1     0 <-- 5    =>    1     1     4
# 第二步:    1 <-- 1 <-- 4    =>    2     1     3
# 第三步:    2     1 <-- 3    =>    2     2     2
#
#
#  示例 2：
#
#
# 输入：machines = [0,3,0]
# 输出：2
# 解释：
# 第一步:    0 <-- 3     0    =>    1     2     0
# 第二步:    1     2 --> 0    =>    1     1     1
#
#
#  示例 3：
#
#
# 输入：machines = [0,2,0]
# 输出：-1
# 解释：
# 不可能让所有三个洗衣机同时剩下相同数量的衣物。
#
#
#
#
#  提示：
#
#
#  n == machines.length
#  1 <= n <= 104
#  0 <= machines[i] <= 105
#
#  Related Topics 贪心 数组
#  👍 84 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """
        衣物数目的均值就是处理后每个位置上的衣物数量，因为多个洗衣机可以同时传递衣物，因此计算每个位置上传递数量的最大值就是总的最大传递数目。
        （必须处理成“左--当前--右”三部分，而不能简单分成左右两部分，因为存在当前位置需要向两边传递的情况）。计算左边处理前后的数量差ldiff，
        右边处理前后的数量差rdiff（ldiff = k*avg - lsumldiff=k∗avg−lsum）。当ldiff>0, rdiff>0ldiff>0,rdiff>0说明左右两边都缺少衣物，
        都需要从i位置传过去，因此次数为ldiff +rdiffldiff+rdiff；ldiff<0, rdiff<0ldiff<0,rdiff<0说明两侧 都余出衣物传到i位置，因为可以
        同时传，次数为max(|ldiff|, |rdiff|)max(∣ldiff∣,∣rdiff∣)，当ldiff, rdiffldiff,rdiff一个大于0，一个小与0时，需要从一侧往
        另一侧传，次数为max(|ldiff|, |rdiff|)max(∣ldiff∣,∣rdiff∣)

        """
        total = sum(machines)
        n = len(machines)
        if total % n: return -1
        avr = total // n
        res = 0
        lsum = 0
        for i in range(n):
            ldiff = i * avr - lsum
            rdiff = (n - i - 1) * avr - (total - lsum - machines[i])
            if ldiff > 0 and rdiff > 0:
                res = max(res, ldiff + rdiff)
            else:
                res = max(res, max(abs(ldiff), abs(rdiff)))
            lsum += machines[i]
        return res


print(Solution().findMinMoves([0, 0, 11, 5]))
