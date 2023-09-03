matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # 4

import numpy as np

class Solution:
    def maximalSquare(self, matrix) -> int:
        matrix = np.array(matrix).astype(int)
        row_indices, col_indices = np.where(matrix == 1)
        ones_index = [[row, col] for row, col in zip(row_indices, col_indices)]
        






import numpy as np

# Create a matrix (2D array) with string "1"
matrix = np.array([["1", "2", "3"],
                   ["4", "1", "6"],
                   ["7", "8", "1"]])

# Convert "1" to 1 in the matrix
converted_matrix = matrix.astype(int)

print("Original matrix:")
print(matrix)

print("\nMatrix with '1' converted to 1:")
print(converted_matrix)

