class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        question:406 medium
        """
        # 按照高度从大到小排序，相同的高度按照位置从小到大排序
        # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        # 首先遍历出所有的数据
        h_dic = {}
        sort_p = []
        res = []

        for i in people:
            if i[0] not in h_dic:
                h_dic[i[0]] = [i]
            else:
                h_dic[i[0]].append(i)

        # 然后将所有的键的值按照k从小到大排列
        for i in h_dic:
            h_dic[i] = sorted(h_dic[i], key=lambda x:x[1])

        # 将所有的键按照从大到小排列

        keys_sort = sorted(h_dic.keys(), reverse=True)

        for i in keys_sort:
            sort_p.extend(h_dic[i])
        for i in sort_p:
            res.insert(i[1], i)
        return res


l = [[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]

s = Solution()
print(s.reconstructQueue(l))
