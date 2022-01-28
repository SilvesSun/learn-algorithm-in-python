# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [
# attacki, defensei] 表示游戏中第 i 个角色的属性。
#
#  如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色
# j ，那么 attackj > attacki 且 defensej > defensei 。
#
#  返回 弱角色 的数量。
#
#
#
#  示例 1：
#
#
# 输入：properties = [[5,5],[6,3],[3,6]]
# 输出：0
# 解释：不存在攻击和防御都严格高于其他角色的角色。
#
#
#  示例 2：
#
#
# 输入：properties = [[2,2],[3,3]]
# 输出：1
# 解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
#
#
#  示例 3：
#
#
# 输入：properties = [[1,5],[10,4],[4,3]]
# 输出：1
# 解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
#
#
#
#
#  提示：
#
#
#  2 <= properties.length <= 10⁵
#  properties[i].length == 2
#  1 <= attacki, defensei <= 10⁵
#
#  Related Topics 栈 贪心 数组 排序 单调栈 👍 73 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # 攻击值从大到小进行排序且按照防御值从小到大开始遍历，这样就可以保证当前已经遍历过的最大防御值角色 qq 的防御值
        #  最大攻击大于当前, 防御肯定大于当前.
        # 记录最大防御值. 也很关键
        # 关键就是一个两圈排序.  防御值是内圈从小到大开始遍历 ,防御值比当前大, 那么肯定外圈变了
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_def = -1
        ans = 0
        for ad, _def in properties:
            # // 攻击力一定不高于之前的 如果之前已经出现过防御力比当前防御值高的, 那么当前角色为弱角色
            if _def < max_def:
                ans += 1
            else:
                max_def = _def
        return ans


if __name__ == '__main__':
    print(Solution().numberOfWeakCharacters([[1,5],[10,4],[4,3]]))