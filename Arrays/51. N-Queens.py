
# https://leetcode.com/problems/n-queens/
class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        # initialise col set
        cols = set()

        # initialise positive diagonals
        # (row + col)
        posDiagonal = set()

        # initialise negative diagonals
        # (row - col)
        negDiagonal = set()

        result = []
        # initialise chess_board with empty spaces marked as "x"
        chess_board = [["."] * n for i in range(n)]

        def backtrack(row):
            # if we found a solution row == n
            if row == n:
                # add the boards and add it to the result
                # make a copy of the board, also note that the output is a string format
                copy_chess_board = ["".join(row) for row in chess_board]
                result.append(copy_chess_board)
                return

            # if base case is not reached, continue to every position to check where we are allowed to place the queen
            for col in range(n):
                if col in cols or (row + col) in posDiagonal or (row - col) in negDiagonal:
                    # skip this position
                    continue
                # if the position is valid
                cols.add(col)
                posDiagonal.add(row + col)
                negDiagonal.add(row - col)
                # make the position
                chess_board[row][col] = "Q"

                # increment the row number
                backtrack(row + 1)

                # undo the previous since we are using back tracking

                cols.remove(col)
                posDiagonal.remove(row + col)
                negDiagonal.remove(row - col)
                # make the position a space
                chess_board[row][col] = "."
            # Call back track passing in the initial value of the row

        backtrack(0)

        return result
