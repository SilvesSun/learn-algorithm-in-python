from pprint import pprint


class Solution(object):
    def solve_n_queens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []

        def is_valid(track, row, col):
            if not track:
                return True
            for i in range(row):
                if track[i][col] == 'Q':  # 本列
                    return False
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:  # 左上
                if track[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:  # 右上
                if track[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        # 路径：board 中小于 row 的那些行都已经成功放置了皇后
        # 选择列表：第 row 行的所有列都是放置皇后的选择
        # 结束条件：row 超过 board 的最后一行
        def backtrack(track, row):

            if len(track) == n:
                res.append(track[:])
                return
            for i in range(n):
                ans = ['.'] * n
                if is_valid(track, row, i):
                    ans[i] = 'Q'
                    track.append(list(ans))
                    backtrack(track, row + 1)
                    track.pop()

        backtrack([], 0)
        res2 = [[] for _ in range(len(res))]
        for index, re in enumerate(res):
            for r in re:
                r_str = "".join(r)
                res2[index].append(r_str)

        return res2


if __name__ == '__main__':
    s = Solution()
    pprint(s.solve_n_queens(4))
