nums = [-4,-1,0,3,10]       # Output: [0,1,9,16,100]

import numpy as np

class Solution:
    def sortedSquares(self, nums):
        nums = np.array(nums)**2
        nums.sort()
        return list(nums)