temperatures = [73,74,75,71,69,72,76,73]        # Output: [1,1,4,2,1,1,0,0]

import numpy as np

class Solution:
    def dailyTemperatures(self, temperatures):      # key_list = [75,71,69,72,76,73] ;   num = 69
        ans_list = [0]
        key_list = [temperatures[-1]]
        ite_list = temperatures.copy()[:-1]
        ite_list.reverse()
        max_valu = key_list[0]
        for num in ite_list:                    # num = ite_list[1:][0]   ;   index = 0
            if num>=max_valu:
                ans_list.insert(0,0)
                max_valu = num
            elif num == key_list[0]:
                ans_list.insert(0,ans_list[0]+1)
            else:
                ans_list.insert(0,np.argmax(np.array(key_list)>num)+1)
            key_list.insert(0,num)

        return ans_list