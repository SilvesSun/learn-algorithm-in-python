class Solution(object):
    def is_possible_divide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < k: return False
        total = sum(nums)
        # 如果总数不能被整除, 说明没法划分
        if total % k != 0: return False
        # 每个桶的值为 total / k
        target = total / k
        # 排序减少判断次数
        # nums.sort()
        # res = [[] for i in range(k)]
        # used 标记已经被使用过的数字
        used = [0] * len(nums)
        s = self.backtrack(k, 0, nums, 0, used, target)
        # print(res)
        return s

    def backtrack(self, k, cur_bucket_total, nums, start, used, target):
        """
        @param k: 待选择的桶编号
        @param cur_bucket_total: 当前桶已经装的数字之和
        @param nums: 待选择的数字列表
        @param used: 已经选择过的索引
        @param start: 开始遍历的位置
        @param target: 目标值
        """
        # 所有桶都被装满了
        if k == 0:
            return True
        if cur_bucket_total == target:
            # 当前桶已经被装满, 开始装下一个桶
            return self.backtrack(k - 1, 0, nums, 0, used, target)
        for i in range(start, len(nums)):
            if used[i]:
                continue

            if nums[i] + cur_bucket_total > target:
                # 当前桶装不下
                continue
            # 选择当前数字
            used[i] = True
            cur_bucket_total += nums[i]

            # 判断下一个数字是否装入当前桶
            if self.backtrack(k, cur_bucket_total, nums, i + 1, used, target):
                return True
            # 否则, 撤销选择
            used[i] = False
            cur_bucket_total -= nums[i]
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.is_possible_divide([4, 5, 3, 2, 5, 5, 5, 1, 5, 5, 5, 5, 3, 5, 5, 2],
                               13))
