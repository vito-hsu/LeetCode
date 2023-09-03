nums = [1,2,3,4]        # Output: [24,12,8,6]
nums = [-1,1,0,-3,3]    # Output: [0,0,9,0,0]

import numpy as np

class Solution:
    def productExceptSelf(self, nums):
        if nums.count(0)>1:
            return [0 for _ in range(len(nums))]
        elif nums.count(0)==1:
            ans_list = [0 for _ in range(len(nums))]
            key_index = nums.index(0)
            nums.remove(0)
            key_value = np.prod(nums)
            ans_list[key_index] = key_value
            return ans_list
        else:
            key_value = np.prod(nums)
            ans_list = []
            for i in range(len(nums)):
                ans_list.append(int(key_value/nums[i]))
            return ans_list
        

ans = Solution()
ans.productExceptSelf(nums=nums)