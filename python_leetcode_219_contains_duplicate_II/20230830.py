nums = [1,2,3,1] ; k = 3         # Output: true
nums = [99,99]   ; k = 2

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if len(nums)<=k:
            if len(set(nums))==len(nums):
                return False
            else:
                return True

        for ind in range(len(nums)-k):
            compare_list = nums[ind:ind+k+1]
            if len(set(compare_list))!=len(compare_list):
                return True
        return False