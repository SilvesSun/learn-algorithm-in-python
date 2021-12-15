# 有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号
# 为 x 的人简称为 "person x "。
#
#  给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱。另给你一个整数数组
#  quiet ，其中 quiet[i] 是 person i 的安静值。richer 中所给出的数据 逻辑自恰（也就是说，在 person x 比 person
#  y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。
#
#  现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是，在所有拥有的钱肯定不少于 person x 的人中，perso
# n y 是最安静的人（也就是安静值 quiet[y] 最小的人）。
#
#
#
#  示例 1：
#
#
# 输入：richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,
# 7,0]
# 输出：[5,5,2,5,4,5,6,7]
# 解释：
# answer[0] = 5，
# person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。
#
# 唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7，
# 但是目前还不清楚他是否比 person 0 更有钱。
# answer[7] = 7，
# 在所有拥有的钱肯定不少于 person 7 的人中（这可能包括 person 3，4，5，6 以及 7），
# 最安静（有较低安静值 quiet[x]）的人是 person 7。
# 其他的答案也可以用类似的推理来解释。
#
#
#  示例 2：
#
#
# 输入：richer = [], quiet = [0]
# 输出：[0]
#
#
#
#  提示：
#
#
#  n == quiet.length
#  1 <= n <= 500
#  0 <= quiet[i] < n
#  quiet 的所有值 互不相同
#  0 <= richer.length <= n * (n - 1) / 2
#  0 <= ai, bi < n
#  ai != bi
#  richer 中的所有数对 互不相同
#  对 richer 的观察在逻辑上是一致的
#
#  Related Topics 深度优先搜索 图 拓扑排序 数组
#  👍 137 👎 0
from collections import deque
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        """
        题目要求找到比自己更有钱的人中最安静的人
        """
        n = len(quiet)
        in_deg = [0] * n
        adj = [set() for _ in range(n)]

        for _from, _to in richer:
            in_deg[_to] += 1
            adj[_from].add(_to)
        # 初始化ans各位为自己
        #         // 题目说的是：在所有拥有的钱肯定不少于 person x 的人中，person y 是最安静的人
        #         // 注意这里的不少于，说明可以是自己
        #
        ans = [i for i in range(n)]

        q = deque([i for i, d in enumerate(in_deg) if d == 0])
        while q:
            # 入度为0的说明更有钱
            p = q.popleft()
            for child in adj[p]:
                # 如果p的安静值比q小，更新p的安静值对应的那个人
                # 注意这里p的安静值，并不是原始的quiet数组中的quiet[p]
                if quiet[ans[p]] < quiet[ans[child]]:
                    ans[child] = ans[p]

                in_deg[child] -= 1
                if in_deg[child] == 0:
                    q.append(child)

        return ans


if __name__ == '__main__':
    print(Solution().loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet=[3, 2, 5, 4, 6, 1, 7, 0]))
