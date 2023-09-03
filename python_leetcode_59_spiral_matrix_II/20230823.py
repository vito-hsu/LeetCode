n = 3       # Output: [[1,2,3],[8,9,4],[7,6,5]]



import numpy as np

class Solution:
    def generateMatrix(self, n: int):
        ans_matrix = np.zeros((n,n), dtype=int)         # ans_matrix[[0,0]]
        key_way = 1
        key_pos = [0,-1]
        start = 1
        while 0 in ans_matrix:
            if key_way%4 == 1:
                while 0 in ans_matrix[key_pos[0],]:
                    row, col = key_pos
                    col += 1
                    key_pos = row, col
                    ans_matrix[row, col] = start
                    start += 1
                key_way += 1
            elif key_way%4 == 2:
                while 0 in ans_matrix[:,key_pos[1]]:
                    row, col = key_pos
                    row += 1            
                    key_pos = row, col
                    ans_matrix[row, col] = start
                    start += 1
                key_way += 1
            elif key_way%4 == 3:
                while 0 in ans_matrix[key_pos[0],]:
                    row, col = key_pos
                    col -= 1                  
                    key_pos = row, col
                    ans_matrix[row, col] = start
                    start += 1
                key_way += 1
            elif key_way%4 == 0:
                while 0 in ans_matrix[:,key_pos[1]]:
                    row, col = key_pos
                    row -= 1                  
                    key_pos = row, col
                    ans_matrix[row, col] = start
                    start += 1
                key_way += 1
        return ans_matrix
    


