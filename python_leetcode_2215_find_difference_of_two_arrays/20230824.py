nums1 = [1,2,3] ; nums2 = [2,4,6]    # Output: [[1,3],[4,6]]

import numpy as np 

class Solution:
    def findDifference(self, nums1, nums2):
        return [np.setdiff1d(nums1, nums2), np.setdiff1d(nums2, nums1)]