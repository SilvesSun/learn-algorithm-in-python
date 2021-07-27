from collections import defaultdict
from pprint import pprint
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for x, y in adjacentPairs:
            d[x].append(y)
            d[y].append(x)
        pprint(d)
        start = -1
        for k, v in d.items():
            if len(v) == 1:
                start = k
                break
        res = [start, d[start][0]]
        n = len(adjacentPairs) + 1
        for _ in range(2, n):
            x = res[-1]
            for y in d[x]:
                if y != res[-2]:
                    res.append(y)
                    break
        return res




if __name__ == '__main__':
    adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
    print(Solution().restoreArray(adjacentPairs))