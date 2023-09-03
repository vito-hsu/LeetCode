nums = [1,1,0,1,1,1]    # Output: 3
nums = [1,0,1,1,0,1]    # Output: 2

import numpy as np

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        nums = np.array(nums)
        zero_indices = np.where(nums == 0)[0]
        zero_indices = np.insert(zero_indices, 0, -1)
        zero_indices = np.insert(zero_indices, len(zero_indices), len(nums))
        key_array = zero_indices[1:]-zero_indices[:-1]-1
        return max(key_array)