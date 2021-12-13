# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
#  示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
#  示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 105
#  -109 <= nums[i] <= 109
#
#  Related Topics 并查集 数组 哈希表
#  👍 1001 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class UF:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.size = {num: 1 for num in nums}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        if y not in self.parent:
            return 1
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return self.size[rootx]
        if self.size[rootx] > self.size[rooty]:
            self.parent[rootx] = rooty
            self.size[rooty] += self.size[rootx]
            return self.size[rooty]
        else:
            self.parent[rooty] = rootx
            self.size[rootx] += self.size[rooty]
            return self.size[rootx]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        uf = UF(nums)
        for num in nums:
            uf.union(num, num + 1)
        return max(uf.size.values())


if __name__ == '__main__':
    print(Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
