
matrix = [[1,1,1],[1,0,1],[1,1,1]]          # Output: [[1,0,1],[0,0,0],[1,0,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]    # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


import numpy as np

class Solution:
    def setZeroes(self, matrix) -> None:
        key_matrix = np.array(matrix)
        row_del = list(set(np.where(key_matrix==0)[0]))
        col_del = list(set(np.where(key_matrix==0)[1]))
        for i in row_del:
            key_matrix[i,:] = 0
        for j in col_del:
            key_matrix[:,j] = 0
        key_matrix = key_matrix.tolist()
        matrix.clear()
        for w in key_matrix:
            matrix.append(w)

            
ans = Solution()
ans.setZeroes(matrix=matrix)