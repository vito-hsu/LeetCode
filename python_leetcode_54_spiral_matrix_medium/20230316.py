matrix = [[1,2,3],[4,5,6],[7,8,9]]              # Output: [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]     # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

import numpy as np

class Solution:
    def spiralOrder(self, matrix):
        matrix = np.array(matrix)
        ans_list = []
        for _ in range(1000):
            if matrix[0,:].tolist()!=[]:
                ans_list.extend(matrix[0,:].tolist())
                matrix = np.delete(matrix, 0, axis=0)
            else:
                break

            if matrix[:,-1].tolist()!=[]:
                ans_list.extend(matrix[:,-1].tolist())
                matrix = np.delete(matrix, -1, axis=1)
            else:
                break

            if matrix[-1,:].tolist()!=[]:
                rev_list = matrix[-1,:].tolist()
                rev_list.reverse()
                ans_list.extend(rev_list)
                matrix = np.delete(matrix, -1, axis=0)
            else:
                break

            if matrix[:,0].tolist()!=[]:
                rev_list2 = matrix[:,0].tolist()
                rev_list2.reverse()
                ans_list.extend(rev_list2)
                matrix = np.delete(matrix, 0, axis=1)
            else:
                break

        return ans_list
