# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # initialise length of row and cols as n since it's a square matrix

        n = len(mat)
        # initialise sum
        sum = 0
        # iterate through ros and cols

        for i in range(n):
            for j in range(n):
                # primary diagonal
                if i == j:
                    sum += mat[i][j]
                # secondary diagonal
                else:
                    if i + j == n - 1 and i != j: # exclude the primary diagonal elements
                        sum += mat[i][j]
        return sum
