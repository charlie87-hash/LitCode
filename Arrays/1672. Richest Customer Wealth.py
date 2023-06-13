# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = []
        # Iterate through each row in the matrix
        for row in accounts:
        # Initialize a variable to store the sum of the row
            row_sum = 0
        # Iterate through each element in the row
            for element in row:
        # Add the element to the row sum
                row_sum += element
            output.append(row_sum)
        return max(output)