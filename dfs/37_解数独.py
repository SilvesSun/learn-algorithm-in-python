from pprint import pprint


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)
        pprint(board)

    def backtrack(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    continue
                for val in range(1, 10):
                    if self.is_valid(board, i, j, str(val)):
                        board[i][j] = str(val)
                        if self.backtrack(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

    def is_valid(self, board, row, col, val):
        # check row
        for i in range(9):
            if board[i][col] == val:
                return False
        for i in range(9):
            if board[row][i] == val:
                return False
        # 3*3小块
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == val:
                    return False
        return True


if __name__ == '__main__':
    board = [["2", ".", "4", ".", ".", ".", ".", ".", "."],
             ["1", ".", "7", ".", "9", ".", ".", ".", "2"],
             [".", ".", ".", ".", ".", ".", "7", ".", "."],
             ["6", ".", ".", ".", ".", "1", ".", ".", "."],
             [".", ".", ".", ".", "2", ".", "6", ".", "3"],
             ["8", ".", "1", ".", "4", "9", ".", ".", "."],
             ["4", ".", ".", ".", "6", ".", ".", "7", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "9"],
             [".", ".", ".", "3", ".", ".", "5", "6", "."]]
    s = Solution()
    s.solveSudoku(board)