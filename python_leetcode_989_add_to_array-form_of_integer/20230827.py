num = [1,2,0,0] ; k = 34    # Output: [1,2,3,4]
num = [2,1,5] ; k = 806     # Output: [1,0,2,1]

import numpy as np

class Solution:
    def addToArrayForm(self, num, k: int):
        k_list      = [int(ele) for ele in list(str(k))]
        if len(num)>len(k_list):
            new_k_list = [0]*(len(num)-len(k_list))
            new_k_list.extend(k_list)
            k_list = new_k_list
        elif len(num)<len(k_list):
            new_num = [0]*(len(k_list)-len(num))
            new_num.extend(num)
            num = new_num
        key_arr     = np.array(num) + np.array(k_list)
        
        ans_list    = []
        key_num     = 0
        for ele in key_arr[::-1]:
            new_ele = key_num + ele    
            if new_ele>9:
                key_num = 1
                ans_list.append(new_ele-10)
            else:
                key_num = 0
                ans_list.append(new_ele)
        if key_num == 1:
            ans_list.append(key_num)
        return ans_list[::-1]