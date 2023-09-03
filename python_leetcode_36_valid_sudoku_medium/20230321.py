board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]   # Output: true

import numpy as np

def check_col(board):
    board = np.array(board)
    for i in range(9):      # i = 0
        col = board[:,i]
        u, c = np.unique(col, return_counts=True)
        a = u!='.' 
        b = c>1
        if sum(1*np.logical_and(a, b))>0:
            print(i,' this col fails')
            return False
    return True

def check_row(board):
    board = np.array(board)
    for i in range(9):      # i = 0
        col = board[i,:]
        u, c = np.unique(col, return_counts=True)
        a = u!='.' 
        b = c>1
        if sum(1*np.logical_and(a, b))>0:
            print(i, ' fails')
            return False
    return True

def check_square_9(board):
    s1 = [board[i][j] for j in range(3) for i in range(3)]
    s2 = [board[i][j] for j in range(3,6) for i in range(3)]
    s3 = [board[i][j] for j in range(6,9) for i in range(3)]
    s4 = [board[i][j] for j in range(3) for i in range(3,6)]
    s5 = [board[i][j] for j in range(3,6) for i in range(3,6)]
    s6 = [board[i][j] for j in range(6,9) for i in range(3,6)]
    s7 = [board[i][j] for j in range(3) for i in range(6,9)]
    s8 = [board[i][j] for j in range(3,6) for i in range(6,9)]
    s9 = [board[i][j] for j in range(6,9) for i in range(6,9)]
    board = np.array([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    for i in range(9):      # i = 4
        col = board[i,:]
        u, c = np.unique(col, return_counts=True)
        a = u!='.' 
        b = c>1
        if sum(1*np.logical_and(a, b))>0:
            print(i,' fails')
            return False
    return True    

class Solution:
    def isValidSudoku(self, board) -> bool:
        if check_col(board=board) and check_row(board=board) and check_square_9(board=board):
            return True
        else:
            return False