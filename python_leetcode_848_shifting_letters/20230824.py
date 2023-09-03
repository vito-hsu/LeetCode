s = "abc" ; shifts = [3,5,9]    # Output: "rpl"
s = "aaa" ; shifts = [1,2,3]    # Output: "gfd"
s = "ruu" ; shifts = [26,9,17]  # 


import string
import numpy as np 

class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        alphabet = list(string.ascii_lowercase)
        number   = [num for num in range(1,26)]
        number.extend([0])
        key_dict1 = {letter:number for letter, number in zip(alphabet, number)}
        key_dict2 = {number:letter for letter, number in key_dict1.items()}
        
        key_value       = sum(shifts)
        ans_string      = ""
    
        for ind in range(len(shifts)):         # num = column_sums[0] ; ind = 0
            # print(ind)
            key_value   = key_value%26
            key_index   = (key_dict1[s[ind]]+key_value)%26
            ans_string  += key_dict2[key_index]
            key_value   -= shifts[ind]

        return ans_string











import numpy as np

input_list = [3, 5, 9]
matrix = np.tril(np.repeat(input_list, len(input_list)).reshape(len(input_list), -1))
column_sums = np.sum(matrix, axis=0)

print("生成的矩阵:\n", matrix)
print("每列的加和:", column_sums)