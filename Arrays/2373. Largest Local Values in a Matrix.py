# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # Create a _grid output initialized with zeros
        _grid = [[0] * (len(grid[0])-2) for _ in range(len(grid)-2)]

        # Iterate over the grid matrix while taking into account the size of the sliding matrix
        for row in range(0, len(grid) - 2):
            for col in range(0, len(grid[0]) - 2):

                max_value = float('-inf')

                # Nested loops to iterate over the 3x3 sliding window
                for i in range(3):
                    for j in range(3):
                        # Find the maximum value in the current sliding window
                        max_value = max(max_value, grid[row + i][col + j])

                # Store the maximum value in the corresponding position in the output grid
                _grid[row][col] = max_value

        # Return the resulting _grid
        return _grid
