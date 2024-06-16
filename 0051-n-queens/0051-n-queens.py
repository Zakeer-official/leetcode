class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_place(board, row, col):
            for i in range(row):
                if col in co or col - row in neg or col + row in pos:
                    return False
            return True

        def place_queen(row):
            if row == n:
                y.append(["".join(i) for i in board])
                return
            for col in range(n):
                if is_place(board, row, col):
                    co.add(col)
                    pos.add(row+col)
                    neg.add(col-row)
                    board[row][col] = "Q"
                    place_queen(row+1)
                    co.remove(col)
                    pos.remove(row+col)
                    neg.remove(col-row)
                    board[row][col] = "."
        y = []
        co = set()
        pos = set()
        neg = set()
        board = [["."] * n for i in range(n)]
        place_queen(0)
        return y