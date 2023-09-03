arr = [0,3,2,1]             # Output: true
arr = [0,1,2,3,4,5,6,7,8,9] # Output: False


import numpy as np

class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(np.where(np.array(arr)==max(arr))[0])>1:
            return False
        
        if len(arr)<3:
            return False

        try:
            split_index = np.argmax(arr)
            key_list1   = np.array(arr)[:split_index]
            if len(key_list1)>1:
                key_list1 = key_list1[1:]-key_list1[:-1]
            else:
                key_list1[0] = 1

            key_list2   = np.array(arr)[split_index+1:]
            if len(key_list2)>1:
                key_list2 = key_list2[:-1]-key_list2[1:]
            else:
                key_list2[0] = 1
        except:
            return False
        
        if min(key_list1)>0 and min(key_list2)>0:
            return True
        else:
            return False
        