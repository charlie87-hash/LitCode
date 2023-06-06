# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:

        # Initialize sets for occupied columns and diagonals
        cols = set()
        posDiagonals = set()
        negDiagonals = set()

        # Create an empty chessboard
        chess_board = [["."] * n for _ in range(n)]

        # List to store solutions
        res = []

        # Counter for the number of valid solutions
        count = 0

        def backtrack(row):
            nonlocal count

            # Base condition: If all queens are placed, increment the count and return
            if row == n:
                count += 1
                return

            for col in range(n):
                # Check if the column or diagonals are already occupied
                if col in cols or (row + col) in posDiagonals or (row - col) in negDiagonals:
                    continue

                # Mark the current position as occupied
                cols.add(col)
                posDiagonals.add(row + col)
                negDiagonals.add(row - col)
                chess_board[row][col] = "Q"

                # Move to the next row
                backtrack(row + 1)

                # Undo the current position
                cols.remove(col)
                posDiagonals.remove(row + col)
                negDiagonals.remove(row - col)
                chess_board[row][col] = "."

        # Start the backtracking process from the first row
        backtrack(0)

        # Return the count of valid solutions
        return count

