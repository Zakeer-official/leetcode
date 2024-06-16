class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_place(board, row , col):
            for i in range(row):
                if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                    return False
            return True
        
        def placed(row):
            if row == n:
                y.append(board[:])
            for col in range(n):
                if is_place(board, row, col):
                    board[row] = col
                    placed(row+1)
                    board[row] = -1
        y = []
        board = [-1] * n
        placed(0)
        return len(y)

        