class Solution(object):
    directs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def exist(self, board, word):
        rows_n = len(board)
        if not rows_n:
            return False
        cols_n = len(board[0])
        visit = [[0 for _ in range(cols_n)] for _ in range(rows_n)]
        print(visit)
        for i in range(rows_n):
            for j in range(cols_n):
                if board[i][j] == word[0]:
                    visit[i][j] = 1
                    if self.backtrack(board, word[1:], visit, i, j) is True:
                        return True
                    else:
                        visit[i][j] = 0
        return False

    def backtrack(self, board, word, mark, i, j):
        if not word:
            return True

        for d in self.directs:
            cur_i = i + d[0]
            cur_j = j + d[1]

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if mark[cur_i][cur_j] == 1:
                    continue
                mark[cur_i][cur_j] = 1
                if self.backtrack(board, word[1:], mark, cur_i, cur_j):
                    return True
                else:
                    mark[cur_i][cur_j] = 0
        return False


if __name__ == '__main__':
    s = Solution()
    s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE")
