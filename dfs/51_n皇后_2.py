from pprint import pprint


class Solution(object):
    def solve_n_queens(self, n):
        # 初始化棋盘
        arr = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def dfs(row):
            if row == n:
                # 说明已经放到最后一行
                res.append(["".join(arr[i]) for i in range(n)])
                return
            # 查看第row行可放置的皇后
            for col in range(n):
                if is_valid(row, col):
                    arr[row][col] = 'Q'
                    dfs(row + 1)
                    arr[row][col] = '.'

        def is_valid(row, col):
            # 判断当前位置是否可以放置皇后
            # 可放置的条件是左右斜边, 当前列不存在皇后

            # 检查当前列
            for i in range(row):
                if arr[i][col] == 'Q':
                    return False

            # 检查左上到右下
            x = row - 1
            y = col - 1
            while x >= 0 and y >= 0:
                if arr[x][y] == 'Q':
                    return False
                x -= 1
                y -= 1

            # 检查右上到左下
            x = row - 1
            y = col + 1
            while x >= 0 and y < n:
                if arr[x][y] == 'Q':
                    return False
                x -= 1
                y += 1
            return True

        dfs(0)
        return res


if __name__ == '__main__':
    s = Solution()
    s.solve_n_queens(4)
