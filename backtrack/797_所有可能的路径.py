class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        path = [0]
        self.backtrack(0, path, res, graph)
        return res

    def backtrack(self, index, path, res, graph):
        if index > len(graph) - 1:
            return
        if len(graph) - 1 == index:
            res.append(path[:])
            return
        dresses = graph[index]
        for i in range(len(dresses)):
            path.append(dresses[i])
            self.backtrack(dresses[i], path, res, graph)
            path.remove(dresses[i])


if __name__ == '__main__':
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    s = Solution()
    print(s.allPathsSourceTarget(graph))
