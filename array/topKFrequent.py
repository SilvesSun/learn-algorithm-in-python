class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        c_dic = {}
        for i in nums:
            if i in c_dic:
                c_dic[i] += 1
            else:
                c_dic[i] = 1
        c_array = []
        for key, v in c_dic.items():
            c_array.append((key, v))

        sort_array = sorted(c_array, key=lambda x: x[1], reverse=True)
        top_frequent = [i[0] for i in sort_array]
        res = []
        for j in range(k):
            res.append(top_frequent[j])
        return res


nums = [-1, -1]
s = Solution()
s.topKFrequent(nums, 1)
