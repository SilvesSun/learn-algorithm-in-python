# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
#
#  给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
#
#  格雷编码序列必须以 0 开头。
#
#
#
#  示例 1:
#
#  输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
#  示例 2:
#
#  输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
#      给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
#      因此，当 n = 0 时，其格雷编码序列为 [0]。
#
#  Related Topics 位运算 数学 回溯
#  👍 329 👎 0
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        codes = []
        path = []

        def backtrack(choice=(0, 1)):
            if len(path) == n:
                codes.append(path[:])
                return
            path.append(choice[0])
            backtrack((0, 1))
            path.pop()

            path.append(choice[1])
            backtrack((1, 0))
            path.pop()
        backtrack((0, 1))

        def decode(code):
            res = 0
            for i in code:
                res = res * 2 + i
            return res
        return list(map(decode, codes))


if __name__ == '__main__':
    print(Solution().grayCode(2))