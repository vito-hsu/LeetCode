nums = [5,7,7,8,8,10]   ;   target = 8   # Output: [3,4]

from bisect import bisect_left,bisect_right

class Solution:
    def searchRange(self, nums, target: int):
        if target in nums:
            return [bisect_left(nums,target), bisect_right(nums, target)-1]
        else: 
            return [-1,-1]
