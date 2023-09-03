mat = [[0,0,0],[0,1,0],[1,1,1]]     # [[0,0,0],[0,1,0],[1,2,1]]
mat = [[0,0,0],[0,1,0],[0,0,0]]     # [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
                                    # [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]


with open(r"C:\Users\vito\Desktop\leetcode_0818.txt", 'r') as file:
    content = file.read()
mat = eval(content)                 # mat.shape


def get_neighbors(matrix, row, col):
    rows, cols = matrix.shape
    neighbors = []
    neighbors.append(matrix[row - 1, col]) if row > 0 else neighbors.append(0)         # up
    neighbors.append(matrix[row, col - 1]) if col > 0 else neighbors.append(0)         # left   
    neighbors.append(matrix[row, col + 1]) if col < cols - 1 else neighbors.append(0)  # right
    neighbors.append(matrix[row + 1, col]) if row < rows - 1 else neighbors.append(0)  # down
    return neighbors



import numpy as np

class Solution:
    def updateMatrix(self, mat):
        mat         = np.array(mat)
        key_mat     = np.array(mat)*0
        ans_mat     = np.array(mat)*0
        key_factor  = 1
        key_mat2    = np.where(mat == 0)
        # rows, cols  = mat.shape
        while 1 in mat:
            # for i in range(rows):           # i = 0
            #     for j in range(cols):       # j = 0
            #         print(i,j)
            #         if mat[i,j] != 0:
            #             continue
                    # else:
            zero_positions  = key_mat2
            zero_indices    = list(zip(zero_positions[0], zero_positions[1]))
            # key_mat2        = []
            for i,j in zero_indices:
                print(i,j)
                up_left_right_down          = get_neighbors(mat,i,j)
                if up_left_right_down       == [0,0,0,0] or key_mat[i,j]>0:
                    continue
                if up_left_right_down[0]    == 1:
                    mat[i-1,j]              = 0
                    key_mat[i-1,j]          += key_factor
                    # key_mat2.append([i-1,j])
                if up_left_right_down[1]    == 1:
                    mat[i,j-1]              = 0
                    key_mat[i,j-1]          += key_factor
                    # key_mat2.append([i,j-1])
                if up_left_right_down[2]    == 1:
                    mat[i,j+1]              = 0
                    key_mat[i,j+1]          += key_factor
                    # key_mat2.append([i,j+1])      
                if up_left_right_down[3]    == 1:
                    mat[i+1,j]              = 0
                    key_mat[i+1,j]          += key_factor
                    # key_mat2.append([i+1,j])
            ans_mat     += key_mat
            key_mat2    =  np.where(key_mat != 0)
            key_mat     *= 0
            key_factor  += 1

        return ans_mat
























import numpy as np

# 创建一个示例矩阵
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 定义一个函数，获取某个元素上、下、左、右的邻近点的值
def get_neighbors(matrix, row, col):
    rows, cols = matrix.shape
    neighbors = []
    
    if row > 0:
        neighbors.append(matrix[row - 1, col])  # 上
    if row < rows - 1:
        neighbors.append(matrix[row + 1, col])  # 下
    if col > 0:
        neighbors.append(matrix[row, col - 1])  # 左
    if col < cols - 1:
        neighbors.append(matrix[row, col + 1])  # 右
    
    return neighbors

row_index = 1
col_index = 1

neighbors = get_neighbors(matrix, row_index, col_index)
print("元素 ({}, {}) 的上、下、左、右邻近点: {}".format(row_index, col_index, neighbors))
















import numpy as np

mat = np.array([[0, 0, 0],
                [0, 1, 0],
                [1, 1, 1]])

# 使用 np.where 来获取值为0的元素的行索引和列索引
zero_positions = np.where(mat == 0)

# 将行索引和列索引合并成一个元组列表
zero_indices = list(zip(zero_positions[0], zero_positions[1]))

print("值为0的元素位置：", zero_indices)
