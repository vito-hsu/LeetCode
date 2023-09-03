# nums = [2,3,1,1,4]  # true
# nums = [3,2,1,0,4]  # false

import numpy as np

class Solution:
    def canJump(self, nums) -> bool:
        ans_list = [True] + [False]*(len(nums)-1)
        ans_list = np.array(ans_list)
        for index, num in enumerate(nums):                     # index = 0 ; num = 3
            if ans_list[index] == True:
                ans_list[index+1:index+num+1] = True
        return ans_list[-1]
    

