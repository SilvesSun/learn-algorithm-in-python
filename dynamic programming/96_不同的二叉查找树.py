# coding:utf-8
__date__ = '2018/6/11 15:54'


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        对于ii, 以k(1≤k≤i)k(1≤k≤i)作为根节点, 左子树的节点为1,...,k−11,...,k−1共有k−1k−1个节点，右子树的节点为k+1,...,ik+1,...,i共有i−ki−k个节点。因此，状态装换方程为
        f(i)=∑ik=1f(k−1)×f(i−k)f(i)=∑k=1if(k−1)×f(i−k)
        """

        res = [0 for _ in range(n+1)]

        res[0] = 1
        i = 1

        while i <= n:
            j = 0
            while j < i:
                res[i] += res[j] * res[i - 1 - j]
                j += 1
            i += 1
        return res[n]


s = Solution()

print(s.numTrees(3))