matrix = [[1,2,3],[4,5,6],[7,8,9]]      # Output: [[7,4,1],[8,5,2],[9,6,3]]


from numpy import rot90

class Solution:
    def rotate(self, matrix):
        key_list = rot90(matrix, k=3).tolist()
        matrix.clear()
        for i in range(len(key_list)):
            matrix.append(key_list[i])
