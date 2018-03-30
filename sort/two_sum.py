class Solution(object):
    def two_sum(self, nums, target):
        index_dic = {}
        for index, i in enumerate(nums):
            if target - i in index_dic:
                return [index_dic[target - i], index]
            index_dic[i] = index